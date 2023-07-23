from genericpath import exists
from tkinter import Y
#import torch
#from torch.utils.data import Dataset
import os
import numpy as np
import cv2
from .Calibration import Calibration
import argparse
import pclpy
import matplotlib.pyplot as plt


class Dataset(object):
    def __init__(self, root_dir, save_dir = None, split="training"):
        """构建数据集

        Args:
            root_dir (_type_): 数据集数据的根目录
            split (str, optional): 数据的分类. Defaults to "training".
        """
        self.root_dir = root_dir
        self.data_path = os.path.join(root_dir, split)

        self.image_dir = os.path.join(self.data_path, "image_2")
        self.lidar_dir = os.path.join(self.data_path, "velodyne")
        self.save_dir = save_dir
        files = os.listdir(self.image_dir) 
        self.num_samples = len(files) 

    def __len__(self):
        """数据的样本数

        Returns:
            _type_: _description_
        """
        return self.num_samples

    def get_image(self, idx):
        """获取对应索引的图像数据

        Args:
            idx (_type_): 图像索引

        Returns:
            _type_: 图像
        """
        assert idx < self.num_samples
        #img_filename = os.path.join(self.image_dir, "%06d.png" % (idx))
        #2022-01-03 前瞻
        img_filename = os.path.join(self.image_dir, "%06d.jpg" % (idx))
        
        return self.load_img_file(img_filename)

    def get_lidar(self, idx):
        """获取对应索引的雷达数据

        Args:
            idx (_type_): 雷达索引

        Returns:
            _type_: 雷达数据
        """
        assert idx < self.num_samples
        
        #lidar_filename = os.path.join(self.lidar_dir, "%06d.pcd" % (idx))
        #2022-01-03 前瞻
        lidar_filename = os.path.join(self.lidar_dir, "%06d.bin" % (idx))
        
        return self.load_lidar_file(lidar_filename)

    def load_img_file(self, filename):
        """用opencv读取图像

        Args:
            filename (_type_): _description_

        Returns:
            _type_: _description_
        """
        return cv2.imread(filename)
    
    def load_lidar_file(self, filename, n_features=4):
        """用pclpy读取pcd

        Args:
            filename (_type_): _description_
            n_features (int, optional): _description_. Defaults to 4.

        Returns:
            _type_: _description_
        """
        if(filename.endswith(".bin")):
            point_clouds = np.fromfile(filename,dtype=np.float32).reshape(-1,4)
            #print("bin:",point_clouds[0:3,0:4])
        
        if(filename.endswith(".pcd")):
            if(n_features == 4):
                pcd_reader = pclpy.pcl.io.PCDReader()
                pc = pclpy.pcl.PointCloud.PointXYZI()
                pcd_reader.read(filename, pc)
                xyz = pc.xyz
                intensity = pc.intensity.reshape(-1, 1)
                point_clouds = np.concatenate([xyz, intensity], axis=1)
        return point_clouds

    def setCalib(self, calib_file):
        """设置投影的标定参数

        Args:
            calib_file (_type_): 标定参数文件路径
        """
        self.calib = Calibration(calib_file)

    def display_all_file_in_dataset(self, display = True, save_file=False):
        """显示dataset中的所有点云投影
        """
        for i in range(self.__len__()):
            self.display_points_on_image(i, display, save_file)

    def display_points_on_image(self, idx, display = True, save_file=False):
        """获取固定索引的点云投影在固定图片

        Args:
            idx (_type_): 图片和点云的索引
        """
        camera_intrinsic_matrix = self.calib.Camera_Intrinsic.intrinsic_matrix
        camera_distortion = self.calib.Camera_Intrinsic.distcoeff
        camera2lidar_trans_matrix = self.calib.Camera_To_Lidar_Extrinsic.tranform_matrix
        halfLidar2lidar_trans_matrix = self.calib.Half_Lidar_To_Lidar_Extrinsic.tranform_matrix


        #lidar2camera_trans_matrix = np.linalg.inv(camera2lidar_trans_matrix)@halfLidar2lidar_trans_matrix
        '''初始化旋转参数
        lidar2camera_trans_matrix =np.array(
        [[ 8.46534955e-03, -9.99836148e-01, -1.60004617e-02,  -2.70983132e-01]
        [-3.85498813e-04,  1.59977707e-02,  -9.99871953e-01,  9.91211857e-02]
        [ 9.99964094e-01,  8.47043374e-03,  -2.50008927e-04,  -6.50130416e-02]
        [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,   1.00000000e+00]])
        '''
        
        '''
        #2022-12-27 外参
        lidar2camera_trans_matrix =np.array(
        [[0.0655953057593969,-0.997803484087253,-0.00924462036382940,0.0244135239073858],
        [0.0415519193873180,0.0119879138408506,-0.999064426309422,0.126538859535614],
        [0.996980789111586,0.0651498047969787,0.0422470008089864,0.0193244422572479],
        [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,1.00000000e+00]])
        '''
        
        #2023-01-03
        lidar2camera_trans_matrix =np.array(
        [[0.0019845240488556497, -0.9985596060657036, -0.05361692641513839, 0.13838509608343585],
        [0.05380678339113221, 0.05364598769072936, -0.9971092909334393, 1.3169114985266877],
        [0.9985493937334293, -0.0009061669785227917, 0.053835742179408515, -1.8975462364217606],
        [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,1.00000000e+00]])
        
        #最新标定的相机外餐 11.1
        # lidar2camera_trans_matrix =np.array([[-0.00737015602984623,-0.999733954369958,-0.0218563784717992,0.0498317472922353],
        # [-0.0179366644207264,0.0219856237016540,-0.999597373155766,0.0322148094219888],
        # [ 0.999811960755398,-0.00697515808108141,0.0180939299266344,0.0781386689346002],
        # [ 0.00000000e+00,0.00000000e+00,0.00000000e+00,1.00000000e+00]])


        

        # lidar2camera_trans_matrix =np.array( [[0.78336333,-0.45040513,0.42834228,-0.0859942676],
        #             [-0.2998801,0.32975789,0.8951713,0.0232642135],
        #             [-0.54443899,-0.8296957,0.12325271,-0.1553790004],
        #             [0,0,0,1]])
        # lidar2camera_trans_matrix = np.linalg.inv(lidar2camera_trans_matrix)

        #lidar2camera_trans_matrix =np.array([[-0.0097,-0.9999,-0.0092,-0.2317],
        #[0.04840023,0.0087849,-0.99870934,0.0772],
        #[0.99870411,-0.01007295,0.04830037,0.16969],
        #[0,0,0,1]])

        #自己标定数据的修改
        #lidar2camera_trans_matrix =np.array([[-0.0097,-0.9999,-0.0092,-0.2717],
        #[-0.0039,0.0093,-0.9999,0.0772],
        #[0.9999,-0.0096,-0.0040,-0.5093],
        #[0,0,0,1]])

        
        print("旋转pingyi:", lidar2camera_trans_matrix)
        lidar_data = self.get_lidar(idx)
        img_data = self.get_image(idx)
        #print("fenbainlv:", img_data.shape)
        lidar_fov_idx, points_in_img = self.get_lidar_points_in_image_fov(lidar_data[:,0:3], lidar2camera_trans_matrix, camera_intrinsic_matrix, img_data)
        points_in_img_with_depth_1 = points_in_img[:,0:2]/np.expand_dims(points_in_img[:,2],-1)
        cmap = plt.cm.get_cmap("hsv", 256)
        cmap = np.array([cmap(i) for i in range(256)])[:, :3] * 255


        #img_dst =cv2.fisheye.undistortImage(img_data,camera_intrinsic_matrix, camera_distortion, camera_intrinsic_matrix)
        #img_dst = cv2.undistort(img_data, camera_intrinsic_matrix, camera_distortion)
        #img_data =img_dst



        for i in range(points_in_img.shape[0]):
            depth = points_in_img[i, 2]
            color = cmap[int(220.0 / depth), :]
            cv2.circle(
                img_data,
                (int(np.round(points_in_img_with_depth_1[i, 0])), 
                    int(np.round(points_in_img_with_depth_1[i, 1]))),
                2,
                color=tuple(color),
                thickness=-1,
            )
        if(save_file):
            lidar_points = lidar_data[lidar_fov_idx]
            rgb_data = np.zeros([lidar_points.shape[0], 3])
            for i in range(lidar_points.shape[0]):
                rgb_data[i,:] = img_data[int(np.round(points_in_img_with_depth_1[i, 1]))][int(np.round(points_in_img_with_depth_1[i, 0]))]
            save_data = np.concatenate([lidar_points, rgb_data], axis=1)
            np.save(os.path.join(self.save_dir, "lidar_rgb_{}.npy".format(idx)), save_data)
        if(display):
            cv2.namedWindow("project",0)
            cv2.imshow("project", img_data)
            key_code = cv2.waitKey(0)
            if key_code & key_code == ord('q'):
                cv2.destroyWindow('project')

    def get_lidar_points_in_image_fov(self, pc_points, transform_matrix, intrinsic_matrix, img, clip_distance=0):
        """获取在图像fov中的点云

        Args:
            pc_points (_type_): 点云,N*3
            transform_matrix (_type_): RT组成的lidar到相机的转化矩阵,4*4
            intrinsic_matrix (_type_): 相机内参矩阵3*3
            img (_type_): 图像
            clip_distance (float, optional): 只选取多少米以前的点. Defaults to 0.

        Returns:
            _type_: _description_
        """
        lidar_points_in_camera = self.get_lidar_points_in_camera_coor(pc_points, transform_matrix)
        lidar_points_in_image = self.get_points_in_camera_to_image_point(lidar_points_in_camera, intrinsic_matrix)
        lidar_points_in_image = lidar_points_in_image
        lidar_points_in_image_with_depth1 = lidar_points_in_image[:,0:2]/np.expand_dims(lidar_points_in_image[:,2],-1)
        img_height, img_width,_= img.shape
        fov_inds = (
            (lidar_points_in_image_with_depth1[:, 0] < img_width-1)
            & (lidar_points_in_image_with_depth1[:, 0] >= 0)
            & (lidar_points_in_image_with_depth1[:, 1] < img_height-1)
            & (lidar_points_in_image_with_depth1[:, 1] >= 0)
        )
        fov_inds = fov_inds & (pc_points[:, 0] > clip_distance)
        return fov_inds, lidar_points_in_image[fov_inds]


    def get_lidar_points_in_camera_coor(self, pc_points, transform_matrix):
        """获取激光雷达的点在相机的3D坐标系下的值

        Args:
            pc_points (_type_): 激光雷达的点:N*3
            transform_matrix (_type_): 4*4的旋转平移矩阵

        Returns:
            _type_: 返回N*3的相机坐标系下的点
        """
        ones_matrix = np.ones([pc_points.shape[0],1])   #N*1
        lidar_home_coor = np.concatenate([pc_points, ones_matrix], axis=1)    #N*4
        points_in_camera = transform_matrix@lidar_home_coor.transpose() #4*4@4*N=4*N
        points_in_camera = points_in_camera.transpose() # 4*N -> N*4
        return points_in_camera[:,0:3]

    def get_points_in_camera_to_image_point(self, points_in_camera, intrinsic_matrix):
        """将在相机3D坐标系下的3D点投影到图像坐标系

        Args:
            points_in_camera (_type_): 在相机坐标系下的3D点,N*3
            intrinsic_matrix (_type_): 相机内参,3*3

        Returns:
            _type_: 像素坐标系下的点    N*3,[x*depth,y*depth,depth]
        """
        points_in_camera = points_in_camera.transpose() #N*3 -> 3*N
        points_in_image = intrinsic_matrix@points_in_camera #3*3@3*N->3*N
        return points_in_image.transpose()

