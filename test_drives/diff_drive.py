#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

rospy.init_node("my_node")
pub=rospy.Publisher("/robot/cmd_vel", Twist, queue_size=1)

vel = Twist()

vel.linear.x = -0.0
vel.angular.z = 0


r=rospy.Rate(1)

while not rospy.is_shutdown():
    pub.publish(vel)
    r.sleep()

    