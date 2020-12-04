import numpy as np
import pickle
import rospy
from std_msgs.msg import Header
import sensor_msgs.point_cloud2 as pcl2
from sensor_msgs.msg import PointField

velo_id = "000000"

# read binary data
scan = (np.fromfile(velo_id + ".bin", dtype=np.float32)).reshape(-1, 4)

# create header
header = Header()
header.frame_id = "world"
header.stamp = rospy.Time.from_sec(123456789)

# fill pcl msg
fields = [PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          PointField('i', 12, PointField.FLOAT32, 1)]
pcl_msg = pcl2.create_cloud(header, fields, scan)

pickle.dump(pcl_msg, open(velo_id + ".p", "wb"))

        
