import numpy as np
import pickle
import rospy
from std_msgs.msg import Header
import sensor_msgs.point_cloud2 as pcl2
from sensor_msgs.msg import PointField

velo_id = "000000"

pcl_msg = pickle.load(open(velo_id + ".p", "rb"))

# print(pcl_msg.header)

        
