#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3
import math

def imu_publisher():
    rospy.init_node('imu_publisher', anonymous=True)
    imu_pub = rospy.Publisher('/imu/data_raw', Imu, queue_size=10)
    rate = rospy.Rate(100) # 100hz

    imu_msg = Imu()
    imu_msg.header.frame_id = 'imu_link'
    imu_msg.orientation_covariance[0] = -1

    for i in range(1000):
        t = float(i)/rate.to_sec()
        ang_vel = Vector3()
        ang_vel.x = math.sin(t)
        ang_vel.y = math.cos(t)
        ang_vel.z = math.sin(2*t)

        lin_acc = Vector3()
        lin_acc.x = math.sin(3*t)
        lin_acc.y = math.cos(2*t)
        lin_acc.z = math.sin(t)

        imu_msg.angular_velocity = ang_vel
        imu_msg.linear_acceleration = lin_acc

        imu_pub.publish(imu_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        imu_publisher()
    except rospy.ROSInterruptException:
        pass
