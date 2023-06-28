#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
import cv2 as cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/front_wide/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)


    img_path="/home/liubo/caic/calib/newcenterright/image"
    timestr = "%.6f" %  data.header.stamp.to_sec()
    cv2.imwrite(img_path+"/"+timestr+".png", cv_image,[cv2.IMWRITE_PNG_COMPRESSION, 0])



def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
