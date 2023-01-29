#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import os
import sys


reached =0
canceled = 0
sequence =1 


def service_node(request):
    global canceled , reached , sequence
    print(f"Sequence: {sequence}\nCanceled: {canceled}\nReached: {reached}")
    print("****")
    sequence += 1
    return EmptyResponse()

def actionserver_subscriber(data):

    if data.status.status == 2:
        global canceled
        canceled += 1
    elif data.status.status == 3:
        global reached
        reached += 1

if __name__ == "__main__":
        rospy.init_node('third')
        rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, actionserver_subscriber)
        rospy.Service('counter', Empty, service_node)
        print("**third**")
        rospy.spin()