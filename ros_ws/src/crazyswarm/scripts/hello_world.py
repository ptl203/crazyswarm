"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm


TAKEOFF_DURATION = 2.5
HOVER_DURATION = 5.0


def main():
    swarm = Crazyswarm() #Represents all crazyflies
    timeHelper = swarm.timeHelper #Timehelper
    cf = swarm.allcfs.crazyflies[0] #Represents a Single crazyflie

    cf.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION) #makes a rosservice call to /takeoff
    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION) #sleeps using rospy 
    cf.land(targetHeight=0.04, duration=2.5) #makes a rosservice call to /land
    timeHelper.sleep(TAKEOFF_DURATION) #sleeps using rospy


if __name__ == "__main__":
    main()
