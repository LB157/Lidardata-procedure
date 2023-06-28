import numpy as np
import os

savedata = []

geometry_path = 'E:\GridVersionPart0_100\geometry'              #0(depth),1(x),2(y),3(z)
intensity_path = 'E:\GridVersionPart0_100\intensity'            #4(intensity)
intensity_bin_path = 'E:\GridVersionPart0_100\intensity'        #5(intensity_bin)
intensity_dist_path = 'E:\GridVersionPart0_100\intensity'       #6(intensity_dist)
label_path = 'E:\GridVersionPart0_100\label'                    #7(label)
color_path = 'E:\GridVersionPart0_100\color'                    #8(R),9(G),10(B)
mask_path = 'E:\GridVersionPart0_100\mask'                      #11(rgb_mask),12(mask)
save_path = 'E:\GridVersionPart0_100\mergdata'                  # for save

for file_name in os.listdir(geometry_path):
    savedata = np.load(geometry_path + '\\' +file_name, encoding="latin1")
    savedata = np.concatenate((savedata, np.load(intensity_path + '\\' + file_name, encoding="latin1")[:, :, None]), axis=2)
    savedata = np.concatenate((savedata, np.load(intensity_bin_path + '\\' + file_name, encoding="latin1")[:, :, None]), axis=2)
    savedata = np.concatenate((savedata, np.load(intensity_dist_path + '\\' + file_name, encoding="latin1")[:, :, None]),axis=2)
    savedata = np.concatenate((savedata, np.load(label_path + '\\' + file_name, encoding="latin1")[:, :, None]),axis=2)
    savedata = np.concatenate((savedata, np.load(color_path + '\\' + file_name, encoding="latin1")[:, :, :]),axis=2)
    savedata = np.concatenate((savedata, np.load(mask_path + '\\' + file_name, encoding="latin1")[:, :, :]),axis=2)
    np.save(save_path + '\\' +file_name, savedata)