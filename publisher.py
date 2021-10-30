#!/usr/bin/env python

import rospy
from std_msgs.msg import String


pub = rospy.Publisher('channel',String, queue_size = 10)
rospy.init_node('publisher_node',anonymous = True)
rate = rospy.Rate(10)


def publisher():
    number = 0
    while not rospy.is_shutdown():
        if number <= 15:
            msg = "hale_dilay :" + number*'*'
            rospy.loginfo(msg)
            pub.publish(msg)
            number += 1
        else:
            number = 0
        rate.sleep()




if __name__ == "__main__":
    publisher()
