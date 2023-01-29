#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from std_srvs.srv import *
import os




def terminal():

    os.system('clear')  
    print("**first**\n")
    print("1:Target :\n")
    print("2:Cancel : \n")   

    input_user = input("select 1 or 2: ")
    
    # Check which number has been chosen
    if   (input_user == "1"):
        target()

    elif (input_user == "2"):
        cancel() 

    else:
        terminal()



def target():
    x = input("\n select x : ")
    y = input(" select y : ")
    x = int(x)
    y = int(y) 
    action_client.wait_for_server()
    print("\nok")
    target_m = PoseStamped()
    target_m.pose.position.x = x
    target_m.pose.position.y = y
    target_m = assignment_2_2022.msg.PlanningGoal(target_m)
    action_client.send_goal(target_m)
    print("\ntarget sent")
    rospy.sleep(2)
    terminal()

def cancel():
    # Used to send cancel requests to servers
    action_client.cancel_goal()
    print("\ncanceled")

    # Sleep for 2 seconds
    rospy.sleep(2)
    terminal()

if __name__ == '__main__':

        rospy.init_node('first')
        action_client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
        terminal()
        rospy.spin()


