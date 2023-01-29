import rospy
from nav_msgs.msg import Odometry
from second_assignment_rt1.msg import odom_custom_msg
import os
import sys


def publisher(data):

    # Publishes a specific type of ROS message
    publishes_robot_data = rospy.Publisher('robot_informations', odom_custom_msg, queue_size=5)


    creat_custom_msg = odom_custom_msg()

    creat_custom_msg.x = data.pose.pose.position.x
    creat_custom_msg.y = data.pose.pose.position.y
    creat_custom_msg.vel_x = data.twist.twist.linear.x
    creat_custom_msg.vel_y = data.twist.twist.linear.y
    
    print(creat_custom_msg)
    # Publishes a specific type of ROS message
    publishes_robot_data.publish(creat_custom_msg)


if __name__ == '__main__':
    try:
        # Initializes a rospy node
        rospy.init_node('custom_msg_node')    
        rospy.Subscriber("/odom", Odometry, publisher)

        # Spin() simply keeps python from existing until this node is stopped
        rospy.spin()
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)


