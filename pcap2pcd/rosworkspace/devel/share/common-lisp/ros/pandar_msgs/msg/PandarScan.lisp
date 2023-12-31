; Auto-generated. Do not edit!


(cl:in-package pandar_msgs-msg)


;//! \htmlinclude PandarScan.msg.html

(cl:defclass <PandarScan> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (packets
    :reader packets
    :initarg :packets
    :type (cl:vector pandar_msgs-msg:PandarPacket)
   :initform (cl:make-array 0 :element-type 'pandar_msgs-msg:PandarPacket :initial-element (cl:make-instance 'pandar_msgs-msg:PandarPacket))))
)

(cl:defclass PandarScan (<PandarScan>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PandarScan>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PandarScan)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pandar_msgs-msg:<PandarScan> is deprecated: use pandar_msgs-msg:PandarScan instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <PandarScan>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pandar_msgs-msg:header-val is deprecated.  Use pandar_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'packets-val :lambda-list '(m))
(cl:defmethod packets-val ((m <PandarScan>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pandar_msgs-msg:packets-val is deprecated.  Use pandar_msgs-msg:packets instead.")
  (packets m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PandarScan>) ostream)
  "Serializes a message object of type '<PandarScan>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'packets))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'packets))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PandarScan>) istream)
  "Deserializes a message object of type '<PandarScan>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'packets) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'packets)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'pandar_msgs-msg:PandarPacket))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PandarScan>)))
  "Returns string type for a message object of type '<PandarScan>"
  "pandar_msgs/PandarScan")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PandarScan)))
  "Returns string type for a message object of type 'PandarScan"
  "pandar_msgs/PandarScan")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PandarScan>)))
  "Returns md5sum for a message object of type '<PandarScan>"
  "70c3ed4f4ae9144323298b04cc2c760b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PandarScan)))
  "Returns md5sum for a message object of type 'PandarScan"
  "70c3ed4f4ae9144323298b04cc2c760b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PandarScan>)))
  "Returns full string definition for message of type '<PandarScan>"
  (cl:format cl:nil "Header header~%PandarPacket[] packets~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: pandar_msgs/PandarPacket~%# field		size(byte)~%# SOB 		2~%# angle		2~%# measure	5~%# block		SOB + angle + measure * 40~%# timestamp	4~%# factory	2~%# reserve	8~%# rpm		2~%# tail		timestamp + factory + reserve + rpm~%# packet	block * 6 + tail~%~%time stamp~%uint8[] data~%uint32 size~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PandarScan)))
  "Returns full string definition for message of type 'PandarScan"
  (cl:format cl:nil "Header header~%PandarPacket[] packets~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: pandar_msgs/PandarPacket~%# field		size(byte)~%# SOB 		2~%# angle		2~%# measure	5~%# block		SOB + angle + measure * 40~%# timestamp	4~%# factory	2~%# reserve	8~%# rpm		2~%# tail		timestamp + factory + reserve + rpm~%# packet	block * 6 + tail~%~%time stamp~%uint8[] data~%uint32 size~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PandarScan>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'packets) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PandarScan>))
  "Converts a ROS message object to a list"
  (cl:list 'PandarScan
    (cl:cons ':header (header msg))
    (cl:cons ':packets (packets msg))
))
