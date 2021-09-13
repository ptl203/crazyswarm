"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm
import time
import rospy
from crazyswarm.srv import *

#Do the hello_world without any helper functions and publishing to the specific topic
#No variables, all hard coded




def main():
    #Make all proxyServices
    rospy.wait_for_service("/cf1/set_group_mask")
    groupMaskService = rospy.ServiceProxy("/cf1/set_group_mask", SetGroupMask)
    rospy.wait_for_service("/cf1/takeoff")
    takeoffService = rospy.ServiceProxy("/cf1/takeoff", Takeoff)
    rospy.wait_for_service("/cf1/land")
    landService = rospy.ServiceProxy("/cf1/land", Land)

    #Takeoff with a height: 1.0, duration: 2.5, groupMask: 0
    print(rospy.Duration.from_sec(2.5))
    takeoffService(0, 1.0, rospy.Duration.from_sec(2.5))
    
    #Sleep 7.5
    rospy.sleep(7.5)

    #Land with a height of 0.4, duration 2.5, groupMask
    landService(0, 0.4, rospy.Duration.from_sec(2.5))

if __name__ == "__main__":
    main()
