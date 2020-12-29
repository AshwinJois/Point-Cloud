# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:08:50 2020

@author: ashwi
"""

from pyntcloud import PyntCloud
import numpy as np
import open3d as o3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

bin_pcd = np.fromfile('Mention ther path/.bin', dtype=np.float32)
# Reshape and drop reflection values
points = bin_pcd.reshape((-1, 4))[:, 0:3]
# Convert to Open3D point cloud
o3d_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))
# Save to whatever format you like
o3d.io.write_point_cloud('Mention ther path/.ply', o3d_pcd)

cloud = PyntCloud.from_file('Path of the cconverted ply file')
cloud.points.keys()

x_points = []
y_points = []
z_points = []

x = cloud.points['x'] 
y = cloud.points['y'] 
z = cloud.points['z'] 

# For removal of unwanted points
"""
for i in range(len(x)):
    
    #if z[i] > -0.5 and z[i] < 0.5:
    info = x[i], y[i], z[i]
    data.append(info)
"""       
for i in range(len(x)):
    #if z[i] > -2.5 and z[i] < 1.5:     
    x_points.append(x[i])
    y_points.append(y[i]) 
    z_points.append(z[i]) 
    
data = (x_points, y_points, z_points)

ax.scatter(data[0], data[1], data[2], s=3)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.view_init(azim=200)
plt.show()







