;; Auto-generated. Do not edit!


(when (boundp 'pandar_msgs::PandarPacket)
  (if (not (find-package "PANDAR_MSGS"))
    (make-package "PANDAR_MSGS"))
  (shadow 'PandarPacket (find-package "PANDAR_MSGS")))
(unless (find-package "PANDAR_MSGS::PANDARPACKET")
  (make-package "PANDAR_MSGS::PANDARPACKET"))

(in-package "ROS")
;;//! \htmlinclude PandarPacket.msg.html


(defclass pandar_msgs::PandarPacket
  :super ros::object
  :slots (_stamp _data _size ))

(defmethod pandar_msgs::PandarPacket
  (:init
   (&key
    ((:stamp __stamp) (instance ros::time :init))
    ((:data __data) (make-array 0 :initial-element 0 :element-type :char))
    ((:size __size) 0)
    )
   (send-super :init)
   (setq _stamp __stamp)
   (setq _data __data)
   (setq _size (round __size))
   self)
  (:stamp
   (&optional __stamp)
   (if __stamp (setq _stamp __stamp)) _stamp)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:size
   (&optional __size)
   (if __size (setq _size __size)) _size)
  (:serialization-length
   ()
   (+
    ;; time _stamp
    8
    ;; uint8[] _data
    (* 1    (length _data)) 4
    ;; uint32 _size
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _stamp
       (write-long (send _stamp :sec) s) (write-long (send _stamp :nsec) s)
     ;; uint8[] _data
     (write-long (length _data) s)
     (princ _data s)
     ;; uint32 _size
       (write-long _size s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _stamp
     (send _stamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _stamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8[] _data
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _data (make-array n :element-type :char))
     (replace _data buf :start2 ptr-) (incf ptr- n))
   ;; uint32 _size
     (setq _size (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get pandar_msgs::PandarPacket :md5sum-) "c29f0f7365a75504f5f0008b5913cb94")
(setf (get pandar_msgs::PandarPacket :datatype-) "pandar_msgs/PandarPacket")
(setf (get pandar_msgs::PandarPacket :definition-)
      "# field		size(byte)
# SOB 		2
# angle		2
# measure	5
# block		SOB + angle + measure * 40
# timestamp	4
# factory	2
# reserve	8
# rpm		2
# tail		timestamp + factory + reserve + rpm
# packet	block * 6 + tail

time stamp
uint8[] data
uint32 size

")



(provide :pandar_msgs/PandarPacket "c29f0f7365a75504f5f0008b5913cb94")


