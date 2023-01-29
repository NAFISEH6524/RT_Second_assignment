
import rospy
from geometry_msgs.msg import PoseStamped
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from std_srvs.srv import *
import os



if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('action_client_node')
        action_client =actionlib.SimpleActionClient('reaching_goal',assignment_2_2022.msg.PlanningAction )
        UI()

	    # Spin() simply keeps python from existing until this node is stopped
        rospy.spin()
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)


def UI():

    os.system('clear')  
    print("_______ USER INTERFACE ________\n")
    print("1)Target pos\n")
    print("2)Cancel\n")   

    input_user = input("Select your operation: ")
    
    # Check which number has been chosen
    if   (input_user == "1"):
        user_goal()

    elif (input_user == "2"):
        cancel() 

    else:
        wrong_input()



def user_goal():


    user_goal_x = input("\n X position: ")
    user_goal_y = input(" Y position: ")
    user_goal_x = int(user_goal_x)
    user_goal_y = int(user_goal_y)
    print(f'\nThe goal position (X,Y): ({user_goal_x},{user_goal_y}) ')
   
 
  
    print("\nThe action server connection is pending")

    # Waits until the action server has started up and started
    # listening for goals.
    action_client.wait_for_server()




    des_goal = PoseStamped()
    des_goal.pose.position.x = user_goal_x
    des_goal.pose.position.y = user_goal_y

    # Creates a custom messagr according to structure of PlanningGoal()
    des_goal = assignment_2_2022.msg.PlanningGoal(des_goal)

    # Sends the goal to the action server.
    action_client.send_goal(des_goal)
    print("\nThe goal was sent to the servers")
    
    # Sleep for 2 seconds
    rospy.sleep(2)

    # Initialize User Interface
    UI()
      


# This function handle cancel option
def cancel():
    # send cancel requests to servers
    action_client.cancel_goal()
    print("\nReaching target canceled by the user")

    # Sleep for 2 seconds
    rospy.sleep(2)
    UI()


# This function handle the wrong inputs 
def wrong_input():

    print("This input is wrong!!!!")

    # Sleep for 2 seconds
    rospy.sleep(2)
    UI()


    


