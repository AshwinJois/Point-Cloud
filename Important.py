# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:08:50 2020

@author: ashwi
"""

from pyntcloud import PyntCloud
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN

cloud = PyntCloud.from_file(r'G:\ICS_Sylabus\Own Projects\004349.ply')
cloud.points.keys()

x_points = []
y_points = []
z_points = []

#data = []

x = cloud.points['x'] 
y = cloud.points['y'] 
z = cloud.points['z'] 

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
"""   
x_points = np.array(x_points)
y_points = np.array(y_points)
z_points = np.array(z_points)
data = (x_points, y_points, z_points)

#data = np.insert(x_points, y_points, z_points)
"""
#data = np.array(cloud.points)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z, c='b', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.view_init(azim=200)
plt.show()

model = DBSCAN(eps=2.5, min_samples=10)
model.fit_predict(data)
pred = model.fit_predict(data)

fig = plt.figure()
ax = Axes3D(fig)
"""
for i in range(len(data)):
    
    ax.scatter(data[i][0], data[i][1], data[i][2], s=3)
"""
#ax.scatter(data[:,0], data[:,1], data[:,2], c=model.labels_,  s=3)
ax.scatter(data[0], data[1], data[2], s=3)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.view_init(azim=200)
plt.show()







