import yaml
import numpy as np
from scipy.spatial.transform import Rotation as R

class Calibration(object):
    def __init__(self, calib_file):
        """标定类，存放内外参

        Args:
            calib_file (str): 标定的配置文件
        """
        self.load_calib_file(calib_file)

    def load_calib_file(self, calib_file):
        """读取标定的配置文件，创建内外参类

        Args:
            calib_file (str): 标定的配置文件
        """
        f = open(calib_file, 'r', encoding='utf-8')
        cfg = f.read()
        param_dict = yaml.load(cfg, Loader=yaml.FullLoader)
        for key, value in param_dict["Intrinsic"].items():
            if(key.startswith("Camera")):
                setattr(self, "{}_Intrinsic".format(key), IntrinsicParam(value))
        for key, value in param_dict["Extrinsic"].items():
            setattr(self, "{}_Extrinsic".format(key), ExtrinsicParam(value))
        
class IntrinsicParam(object):
    def __init__(self, param_dict, type="camera")->None:
        """内参类

        Args:
            param_dict (dict): 内参的参数字典
            type (str, optional): 指定的传感器类型，目前只支持相机. Defaults to "camera".
        """
        self.intrinsic_matrix = np.asarray(param_dict["Intrinsic"])
        self.distcoeff = np.asarray(param_dict["Distcoeff"])

class ExtrinsicParam(object):
    def __init__(self, param_dict, type="quaternion") -> None:
        """外参类

        Args:
            param_dict (dict): 外参的参数字典
            type (str, optional): 可以支持输入四元数或者直接旋转矩阵，目前只支持四元数. Defaults to "quaternion".

        Raises:
            NotImplementedError: _description_
        """
        if(type=="quaternion"):
            self.quaternion = np.asarray(param_dict["Quaternion"])    
            self.rotation_matrix = self.quaternion2rotation_matrix(self.quaternion) #3*3
            self.translation = np.asarray(param_dict["Translation"])    #3*1
        else:
            raise NotImplementedError
        self.get_transform_matrix()

    def get_transform_matrix(self)->None:
        """通过旋转矩阵和平移矩阵获取转换矩阵
             R |T
            000|1
        """ 
        self.tranform_matrix = np.concatenate([self.rotation_matrix, self.translation], axis=1)    #3*4
        #再加一行[0,0,0,1]
        self.tranform_matrix = np.concatenate([self.tranform_matrix, np.array([[0,0,0,1]])], axis=0)

    @staticmethod
    def quaternion2rotation_matrix(quaternion)->np.ndarray:
        """四元数转旋转矩阵

        Args:
            quaternion (List or np.ndarray): 四元数(w,x,y,z)

        Returns:
            np.ndarray: 旋转矩阵:3*3
        """
        rotation = R.from_quat(quaternion)
        rotation_matrix = rotation.as_matrix()
        return rotation_matrix