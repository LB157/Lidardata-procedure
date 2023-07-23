import os
import sys
sys.path.append(".")
from lidar_rgb.DataSet import Dataset
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--split',default="training",help='training or testing')
    parser.add_argument('--sava_lidar_rgb',default = True,help='save npy')
    parser.add_argument('--display_lidar_rgb',default = False,help='save npy')
    args = parser.parse_args()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    kitti_dataset = Dataset(os.path.join(BASE_DIR, "../data"), os.path.join(BASE_DIR, "../Savedata"),)
    kitti_dataset.setCalib(os.path.join(BASE_DIR, "../config/config.yml"))
    kitti_dataset.display_all_file_in_dataset(args.display_lidar_rgb, args.sava_lidar_rgb)
    #2022-01-03 前瞻
    #kitti_dataset.display_all_file_in_dataset(args.display_lidar_rgb)