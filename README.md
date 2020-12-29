# Autonomous Driving


The self driving vehicles that does not involve human intervention is known as Autonomous Driving. An exponential increase of the vehicles on the streets have raised concerns associated
with traffic congestion, the safety of road users and fatal road accidents. These key issues
have resulted in an increased demand for Autonomous Driving (AD). Despite stringent
government regulations, complete safety of road users is still not guaranteed. These issues
can be addressed by introducing the technology-driven solution called as Advanced Driver
Assistance System (ADAS)

The term ADAS defines vehicle-based intelligent systems which assists the driver
in the driving process. ADAS reduces driving effort with precision driving, efficient
performance and enhanced safety. The main objective of ADAS is to ensure safety for
all road users. ADAS can guide drivers in terms of crash avoidance, intelligent speed
adaptation, advanced braking systems, lane assistance and have the potential to prevent
major risks involved in transportation

A complete visual perception of the surrounding environment is needed for ADAS to
ensure good performance. A human being or an animal understands the environment
around by evaluating signals from different senses, like vision, sound, touch, and feel.
Likewise, we use several sensors around the ego vehicle to perceive the 3D environment.
The common sensors used in the automotive field are cameras, radars, ultrasonic sensors,
LiDAR, position estimators and Electronic Control Unit (ECU). Sometimes, the sensor
data is recorded individually and processed to understand the behavior of the objects
around. Mostly, the data from several sensors are fused together, calibrated against each
other and then the fused data is analyzed and evaluated. The fused data has increased
confidence, improved resolution, reduced ambiguity and robustness against interference
It is a set of data points in space whcih represents 3D shape of an object. Each point in the point cloud has its own X, Y and Z coordinates. 


**ADAS Sensors:**

CAMERA

For high precision automated driving,
rear and 360°camera supports the driver with a better understanding of the surrounding
region. Mostly, 2D cameras are used for sensing the environment. Some automotive
companies also use a virtual 3D display to enhance the user experience. To produce
realistic 3D images, data from at least 4 to 6 cameras are required.

RADAR

RADARs use electromagnetic waves to localize and detect the presence of an object or
an obstacle. RADARs have been used in the automotive industry for a long time. It
can determine velocity, range, range doppler maps and angle. It works well even in poor
lighting conditions. The main drawback is that it finds it complicated to identify and
classify the detected object or an obstacle

LIDAR

LiDAR is a newly introduced sensor in the automotive industry. A lot of automobile
manufacturers are investing huge money and time in the production and data analysis
of LiDAR. The LiDAR sensor makes use of a laser beam as the source and has a highly
sensitive receiver. It can measure distances to objects and obstacles even when they are
in motion. The LiDAR sensor provides a complete 360°coverage using a single unit. A set
of 3D point coordinates of the surrounding is generated. LiDAR has better performance
even in poor weather conditions, and it is not sensitive to low light. Processing LiDAR
data is simpler than processing multiple camera data.


**Kitti Dataset**

The kitti dataset consists of the data recorded by multiple sensors fitted on the car. The data was recorded for 6 hours of traffic scenarios using variety of sensors such as camera, Velodyne Lidar sensor. For more inforation check http://www.cvlibs.net/datasets/kitti/. Since the main purpose of this repository is to know how the lidar data is distributed, let us unwrap the laser information of Velodyne. Download the velodyne point clouds which is of 29 GB.
The Velodyne laser information is stored as .bin file. In order to understand the lidar pings distribution, let us plot it first.


![s=3](https://user-images.githubusercontent.com/63425115/103249677-ab0f3f00-4970-11eb-867d-6c70cd1f209f.png)


The above figure shows the dsitribution of the lidar pings. Each ping has its own X, Y, Z coordinates. In order to have a better understanding of the distribution, let us rotate the plot and try to comprehend. 

![Capture](https://user-images.githubusercontent.com/63425115/103250196-07735e00-4973-11eb-9e88-20dd7b178538.JPG)

The above plot shows clearly how the lidar pings are being distributed among several obstacles such as car, persons, other obstacles and finally the ground reflections. Not all the pings are important such as pings from the wall, barriers on the road and also the reflection from the ground. In the plot the circular pattern represents the ground reflection. Removal of ground reflections are very important.
