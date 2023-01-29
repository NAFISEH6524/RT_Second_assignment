#! /usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from npackage.msg import custom_msg
import os


def publisher(data):
    publishes_robot_data = rospy.Publisher('msg_data', custom_msg, queue_size=5)
    msg = custom_msg()

    msg.x = data.pose.pose.position.x
    msg.y = data.pose.pose.position.y
    msg.vel_x = data.twist.twist.linear.x
    msg.vel_y = data.twist.twist.linear.y
    publishes_robot_data.publish(msg)

if __name__ == '__main__':
        rospy.init_node('second')    
        rospy.Subscriber("/odom", Odometry, publisher)
        print("**second**")
        rospy.spin()



