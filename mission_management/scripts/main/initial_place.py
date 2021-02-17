#!/usr/bin/env python 
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback 

def feedback_callback(feedback):
	print('[Feedback] going to goal pose...')


if __name__ == "__main__":
	rospy.init_node("send_a_goal")

	#connect to a action server called '/move_base'
	client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
	
	client.wait_for_server()

	my_goal = MoveBaseGoal()
	my_goal.target_pose.header.frame_id = "map"
	my_goal.target_pose.pose.position.x= -29.452327
	my_goal.target_pose.pose.position.y= -42.9307
	my_goal.target_pose.pose.orientation.z=0.426637
	my_goal.target_pose.pose.orientation.w = 0.905

	client.send_goal(my_goal, feedback_cb = feedback_callback)
	rospy.loginfo("A goal has been sent.")

	client.wait_for_result()
	rospy.loginfo(client.get_state())

	if rospy.ROSInterruptException:
		rospy.loginfo("Robot has arrived at the initial point")
	else:
		rospy.spin()
