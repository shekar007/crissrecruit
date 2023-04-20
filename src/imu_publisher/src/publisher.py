#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3

def imu_publisher():
    rospy.init_node('imu_publisher', anonymous=True)
    imu_pub = rospy.Publisher('/imu/data_raw', Imu, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    imu_msg = Imu()
    imu_msg.header.frame_id = 'imu_link'
    imu_msg.orientation_covariance[0] = -1

    lin_acc = Vector3()
    lin_acc.x = 2.5
    lin_acc.y = 0
    lin_acc.z = 9.8

    for i in range(100):
        ang_acc = Vector3()
        ang_acc.x = 0
        ang_acc.y = 0
        ang_acc.z = i/10.0

        imu_msg.angular_velocity = ang_acc
        imu_msg.linear_acceleration = lin_acc

        imu_pub.publish(imu_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        imu_publisher()
    except rospy.ROSInterruptException:
        pass
