#实现单帧pcd通过rviz可视化   
mkdir de_ws  
cd de_ws  
mkdir src   
cd src   
catkin_init_workspace  
cd ..  
catkin_make  
catkin_make install  
cd src  
catkin_create_pkg read_pcd pcd_conversions pcl_ros roscpp sensor_msgs  
cd ..  
catkin_make  
source devel/setup.bash  
roscore
rosrun read_pcd read_pcd  

