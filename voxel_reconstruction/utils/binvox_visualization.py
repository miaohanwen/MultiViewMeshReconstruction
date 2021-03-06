# -*- coding: utf-8 -*-
#
# Developed by Haozhe Xie <cshzxie@gmail.com>

import cv2
import matplotlib.pyplot as plt
import os

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d


def get_volume_views(volume, save_dir, idx1, idx2):
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)

    volume = volume.squeeze().__ge__(0.5)
    fig = plt.figure()
    ax = fig.gca(projection=Axes3D.name)
#     ax.set_aspect('equal')
#     ax = fig.add_subplot((111), aspect='equal', projection='3d')
#     ax.scatter((1, 2), (1, 1.2), (1, 2)) 
    ax.voxels(volume, edgecolor="k")

    save_path = os.path.join(save_dir, 'voxels-%02d-%02d.png' % (idx1, idx2))
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()
    return cv2.imread(save_path)
