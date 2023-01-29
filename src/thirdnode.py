import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import os
import sys


reached_goal_count =0
canceled_goal_count = 0
sequence =1 


def service_node(request):
    global canceled_goal_count , reached_goal_count , sequence
    print(f"Sequence: {sequence}\nNumber of canceled goal: {canceled_goal_count}\nnumber of reached goal: {reached_goal_count}")
    print("****")
    sequence += 1
    return EmptyResponse()
    
def actionserver_subscriber(data):

    if data.status.status == 2:

        global canceled_goal_count
        canceled_goal_count += 1
    
    elif data.status.status == 3:

        global reached_goal_count
        reached_goal_count += 1


if __name__ == "__main__":
    try:
        # Writing log messages
        rospy.logwarn("service started")

        # Initializes a rospy node
        rospy.init_node('service_node')

        rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, actionserver_subscriber)

        rospy.Service('reach_cancel_ints', Empty, service_node)

        # Spin() simply keeps python from existing until this node is stopped
        rospy.spin()
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
