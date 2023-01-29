import math
from second_assignment_rt1.msg import odom_custom_msg
import rospy
import os
import sys

count =0
velocity =0
average_velocity =0
distance=0


def subscriber(data):

    global count
    global velocity
    global average_velocity
    global distance

    desire_pos_x = rospy.get_param("/des_pos_x")
    desire_pos_y = rospy.get_param("/des_pos_y")

    current_x = data.x
    current_y = data.y

    distance= math.sqrt(((desire_pos_x - current_x)**2)+((desire_pos_y - current_y)**2))
	 current_x_velocity = data.vel_x
    current_y_velocity = data.vel_y

    currrent_velocity= math.sqrt((current_x_velocity**2)+(current_y_velocity**2))

    if count<5:

        velocity=velocity+currrent_velocity
        count +=1

    elif count==5:

        count=0
        velocity /= 5
        average_velocity=velocity
        velocity=0


def print_velocity():
        
        while True:
            print(f"distance of robot to goal: {distance : .3f}")
            print(f'average velocity of robot: {average_velocity: .3f}')
            rate.sleep()
	

if __name__ == "__main__":
    try:
        # Writing log messages
        rospy.logwarn("subscriber_position_node started")

        # Initializes a rospy node
        rospy.init_node('subscriber_position_node')

        # Read the data per second
        rate = rospy.Rate(rospy.get_param("/print_per_second"))
	
        rospy.Subscriber("robot_informations", odom_custom_msg, subscriber)
        
        print_velocity()

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
