#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8

if __name__ == "__main__":
	rospy.init_node("led7seg_talker")
	pub = rospy.Publisher("led7seg", Int8, queue_size=10)
	i = 0
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		rospy.loginfo("echo "+str(i))
		pub.publish(i)
		i += 1
		if i > 9:
			i = 0
		rate.sleep()	
