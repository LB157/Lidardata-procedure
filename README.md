激光雷达数据包、标定处理  
ROS_PCD_png：  
Ros_png:可能是将rosbag包中视频转化为png  
catkin_ws:处理rosbag文件，接收者生成pcd文件  
de_ws:单帧pcd通过rviz可视化  
lidar-RGB：点云和图像通过标定矩阵进行匹配对齐  
mkv2png:将mkv处理为png  
rosworkspace：禾赛专用的通过ros处理pcap包的udp协议  
