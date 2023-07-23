from distutils.command.config import config
import os
from pickle import NONE
import yaml
import numpy as np
#当前路径
#YamlReader


class CameraMatrix(object):
    
    def __init__(self):
        current_path = os.path.abspath(os.path.dirname(__file__))
        #print(current_path)
        #配置文件路径
        yamlPath = os.path.join(current_path+"/config"+"/", "config_yaml.yml")
        #print(yamlPath)
        #print(yamlPath)
        f = open(yamlPath, 'r', encoding='utf-8')
        cfg = f.read()
        params = yaml.load(cfg, Loader=yaml.FullLoader)
        #ff=params['y']
        self.Rotation=np.array(params['R']).reshape(3,3)
        Trans=np.array(params['T']) 
    #print("one line:",Rotation.shape)
        self.Translation=Trans.reshape(Trans.shape[0],1)
    #print("one line平移:",Translation.shape)
    #transpose(1,0)
        self.Internal=np.array(params['K']).reshape(3,3)

    def pts3d_matrixhom(self,pts_3d):
        """_summary_
        Args:
            pts_3d (_type_): 原始点云坐标xyz n*3
        Returns:
            _type_: 齐次化处理，原始点云  n*4  列增加一
        """
        n = pts_3d.shape[0]
        pts_3d_hom = np.hstack((pts_3d, np.ones((n, 1))))
        return pts_3d_hom


    def K_matrixhom(self,Inter):
        """_summary_

        Args:
            Inter (_type_): _相机内参_  3*3

        Returns:
            _type_: _齐次化相机内参_     3*4
        """
        n = Inter.shape[0]
        Inter_hom = np.hstack((Inter, np.ones((n, 0))))
        return Inter_hom
        

    #print("test_first:",matrixhom(Rotation))



    def matrixhom_Rt(R,t):
        """_summary_

        Args:
            R (_type_): _旋转矩阵_  3*3
            t (_type_): _平移矩阵_  3*1

        Returns:
            _type_: _齐次化的旋转平移矩阵Rt_   4*4
        """
        Rt = np.hstack((R,t))
        Rt_hom= np.vstack((Rt, np.array([0,0,0,1])))
        return Rt_hom

#class_instance = CameraMatrix()
#    print("齐次化相机内参：",K_matrixhom(Internal))
#    print("齐次化相机外参：",matrixhom_Rt(Rotation,Translation))

#print("two line:",Rotation)
#print("three line:",rr)