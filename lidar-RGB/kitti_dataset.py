from tkinter import Y
import torch
from torch.utils.data import Dataset
import sys
import os
import numpy as np
import cv2
import kitti_util as utils
import argparse
#import mayavi.mlab as mlab


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)
ROOT_DIR = os.path.dirname(BASE_DIR)

class KittiClass(object):
    def __init__(self, root_dir, split="training"):
        self.data_path = os.path.join(root_dir, split)
        #print(lidar_path, split)
     
        if split == "training":
            self.num_samples = 3
        ''' elif split == "testing":
            self.num_samples = 7518
        else:
            print("Unknown split: %s" % (split))
            exit(-1)
        '''
        self.image_dir = os.path.join(self.data_path, "image_2")
        self.calib_dir = os.path.join(self.data_path, "calib")
        self.lidar_dir = os.path.join(self.data_path, "velodyne")

    def __len__(self):
        return self.num_samples

    def get_image(self, idx):
        assert idx < self.num_samples
        img_filename = os.path.join(self.image_dir, "%06d.png" % (idx))
        return utils.load_image(img_filename)

    def get_lidar(self, idx, dtype=np.float32, n_vec=4):
        assert idx < self.num_samples
        lidar_filename = os.path.join(self.lidar_dir, "%06d.bin" % (idx))
        print(lidar_filename)
        return utils.load_velo_scan(lidar_filename, dtype, n_vec)

    def get_calibration(self, idx):
        assert idx < self.num_samples
        calib_filename = os.path.join(self.calib_dir, "%06d.txt" % (idx))
        return utils.Calibration(calib_filename)
#print(get_calibration(1))


def get_lidar_in_image_fov(
    pc_velo, calib, xmin, ymin, xmax, ymax, return_more=False, clip_distance=2.0
):
    """ Filter lidar points, keep those in image FOV """
    pts_2d = calib.project_velo_to_image(pc_velo)
    fov_inds = (
        (pts_2d[:, 0] < xmax)
        & (pts_2d[:, 0] >= xmin)
        & (pts_2d[:, 1] < ymax)
        & (pts_2d[:, 1] >= ymin)
    )
    fov_inds = fov_inds & (pc_velo[:, 0] > clip_distance)
    imgfov_pc_velo = pc_velo[fov_inds, :]
    # pts_2d = pts_2d[fov_inds, :]
    if return_more:
        return imgfov_pc_velo, pts_2d, fov_inds
    else:
        return imgfov_pc_velo

'''
def get_lidar_index_in_image_fov(
    pc_velo, calib, xmin, ymin, xmax, ymax, return_more=False, clip_distance=2.0
):
    """ Filter lidar points, keep those in image FOV """
    pts_2d = calib.project_velo_to_image(pc_velo)
    fov_inds = (
        (pts_2d[:, 0] < xmax)
        & (pts_2d[:, 0] >= xmin)
        & (pts_2d[:, 1] < ymax)
        & (pts_2d[:, 1] >= ymin)
    )
    fov_inds = fov_inds & (pc_velo[:, 0] > clip_distance)
    return fov_inds
'''
def show_lidar_on_image(pc_velo, img, calib, img_width, img_height):
    """ Project LiDAR points to image """
    img =  np.copy(img)
    imgfov_pc_velo, pts_2d, fov_inds = get_lidar_in_image_fov(
        pc_velo, calib, 0, 0, img_width, img_height, True
    )
    imgfov_pts_2d = pts_2d[fov_inds, :]
    imgfov_pc_rect = calib.project_velo_to_rect(imgfov_pc_velo)
    import matplotlib.pyplot as plt
    cmap = plt.cm.get_cmap("hsv", 256)
    cmap = np.array([cmap(i) for i in range(256)])[:, :3] * 255

    for i in range(imgfov_pts_2d.shape[0]):
        depth = imgfov_pc_rect[i, 2]
        color = cmap[int(640.0 / depth), :]
        cv2.circle(
            img,
            (int(np.round(imgfov_pts_2d[i, 0])), int(np.round(imgfov_pts_2d[i, 1]))),
            2,
            color=tuple(color),
            thickness=-1,
        )

    return img



def sava_lidar_rgb(idx,pc_velo, img, calib, img_width, img_height):
    img =  np.copy(img)
    # savedata = []s
    imgfov_pc_velo, pts_2d, fov_inds = get_lidar_in_image_fov(
        pc_velo, calib, 0, 0, img_width, img_height, True
    )
    imgfov_pts_2d = pts_2d[fov_inds, :]
    savedata = np.zeros([imgfov_pts_2d.shape[0], 3])
    save_path = '/home/liubo/personal/project/lidar-RGB/Savedata/'  
    #右边x=width  下是y=height
    #print("yanse:",img.shape)
    
    for i in range(imgfov_pts_2d.shape[0]):
        #print(type(i))
        r=img[int(imgfov_pts_2d[i, 1]), int(imgfov_pts_2d[i, 0]),0]
        g=img[int(imgfov_pts_2d[i, 1]), int(imgfov_pts_2d[i, 0]),1]
        b=img[int(imgfov_pts_2d[i, 1]), int(imgfov_pts_2d[i, 0]),2]
        rgb=np.array([r,g,b])
        savedata[i,:]=rgb
    print("rgb维度：",savedata.shape)   
    savedata = np.concatenate((imgfov_pc_velo,savedata),axis=1)
    print("拼接的维度：",savedata.shape)  
    #rgb=img[148,107]
    #3 141 0 230 255
    #savedata = np.concatenate((imgfov_pc_velo, np.load(mask_path + '\\' + file_name, encoding="latin1")[:, :, :]),axis=2)
    np.save(save_path +"%06d" % (idx), savedata)
    print(idx," imgfov_pc_velo shape: ", imgfov_pc_velo.shape)
    print(idx," imgfov_pts_2d  shape: ", imgfov_pts_2d.shape)











def dataset_viz(root_dir, args=None):
    #/home/liubo/anaconda3/envs/kitti_rgb/bin/python /home/liubo/Downloads/lidar-RGB/kitti_dataset.py --split training    
    dataset = KittiClass(root_dir, split=args.split)
    ## load 2d detection results
    #objects2ds = read_det_file("box2d.list")
    for data_idx in range(len(dataset)):
        if args.split == "training":
            n_vec = 4
        dtype = np.float32
        pc_velo = dataset.get_lidar(data_idx, dtype, n_vec)[:, 0:n_vec]
        calib = dataset.get_calibration(data_idx)
        img = dataset.get_image(data_idx)
        img_height, img_width, _ = img.shape
        print(data_idx, "image shape: ", img.shape)
        print(data_idx, "velo  shape: ", pc_velo.shape)

    
        sava_lidar_rgb(data_idx,pc_velo[:, 0:3], img, calib, img_width, img_height)
        #if args.show_lidar_on_image:
      
            # Show LiDAR points on image.
        img = show_lidar_on_image(pc_velo[:, 0:3], img, calib, img_width, img_height)
        cv2.imshow("project", img)
        key_code = cv2.waitKey(0)

        if key_code & key_code == ord('q'):
            continue
        input_str = input()
        cv2.destroyAllWindows()
        #mlab.clf()
        if input_str == "killall":
            break


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--split',default="training",help='training or testing')
    parser.add_argument('--sava_lidar_rgb',default = True,help='save npy')
    parser.add_argument('--show_lidar_on_image',default = True, help='training or testing')
    args = parser.parse_args()
    #import mayavi.mlab as mlab
    dataset_viz(ROOT_DIR, args)




'''
class KittiDataset(Dataset):
    def __init__(self, data_root, split="training") -> None:
            super().__init__()
            self.data_path = os.path.join(data_root, split)
            self.lidar_path = os.path.join(self.data_path, "velodyne")
            #找一下这个dir里面有多少文件
            self.length = N


    def __getitem__(self, index):
        pc_file = os.path.join(self.lidar_path, "%06d" % index)
        points = np.fromfile(pc_file)
        #image
        #label
        #calib
        points_fov = 0  #[N*4],N是在图像上的点云个数
        points_fov_in_image = calib.lidar2rect()    #[N*2]
        points_fov_in_image.int()
        image_fov = image[points_fov_in_image[0], [1]] #[N*3]
        res_points = np.concatenate([points_fov, image_fov],axis=1)


        res_dict = {}
        res_dict["points"] = points_fov
        res_dict["appended_points"]= res_points



        return res_dict

    def __len__(self):
        return self.length
'''