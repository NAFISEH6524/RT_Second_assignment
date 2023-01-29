#!/usr/bin/env python3


import math
from npackage.msg import custom_msg
import rospy
import os

i =0
v =0
avg_v =0
d=0


def subscriber(data):

    global i
    global v
    global avg_v
    global d

    x_goal = rospy.get_param("/des_pos_x")
    y_goal = rospy.get_param("/des_pos_y")

    x_cur = data.x
    y_cur = data.y

    d= math.sqrt(((x_goal - x_cur)**2)+((y_goal - y_cur)**2))

    x_v_cur = data.vel_x
    y_v_cur = data.vel_y

    v_cur= math.sqrt((x_v_cur**2)+(y_v_cur**2))

    if i<5:
        v=v+v_cur
        i +=1
    elif i==5:
        i=0
        v /= 5
        avg_v=v
        v=0

def print_velocity():
        
        while True:
            os.system('clear')
            print("**fourth**")
            print(f"distance of robot to goal: {d : .3f}")
            print(f'average velocity of robot: {avg_v: .3f}')
            rate.sleep()
	

if __name__ == "__main__":
        rospy.init_node('fourth')
        freq = rospy.get_param("/freq")
        rate = rospy.Rate(freq)
        rospy.Subscriber("msg_data", custom_msg, subscriber)
        print_velocity()



