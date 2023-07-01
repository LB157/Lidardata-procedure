发布者利用ROS提取.bag的pointcloud2信息，接收者根据信息生成pcd文件  
roslaunch pcd_reader pcd_writer.launch ros_bag_file:=/home/liubo//caic/calib/centercenter/centercenter_2022-09-30-10-38-10_0.bag  
roslaunch pcd_reader pcd_writer.launch ros_bag_file:=/home/liubo//caic/calib/leftdown/leftdown_2022-09-30-10-32-14_0.bag
利用禾赛at128的udp作为发布者，通过此程序作为接收者，处理pointcloud2的点云信息，生成pcd文件  
source devel/setup.zsh  
rosrun pcd_reader pcd_reader_writer


