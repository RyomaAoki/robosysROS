#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8

def led7seg(number):
	try:
		with open("/dev/myled0", "w") as f:
			f.write(str(number)+"\n")
	except IOError:
		rospy.logerr("cannot write")

def callback(msg):
	led7seg(msg.data)

if __name__ == "__main__":
	rospy.init_node("led7seg_listener")
	rospy.Subscriber("led7seg", Int8, callback)
	rospy.spin()
