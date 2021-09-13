#include "ros/ros.h"
#include "crazyswarm/Takeoff.h"
#include "crazyswarm/Land.h"

/**
This should have the crazyflie launch, hover, and land then close node
**/

int main(int argc, char **argv) {
    //Init Node
    ros::init(argc, argv, "hello_crazyflie");
    ros::NodeHandle n;

    //Set Loop Rate
    ros::Rate loop_rate(10);

    ROS_INFO("Creating Clients");
    ros::ServiceClient takeoffClient = n.serviceClient<crazyswarm::Takeoff>("/cf1/takeoff");
    ros::ServiceClient landClient = n.serviceClient<crazyswarm::Land>("/cf1/land");
    
    //Call Takeoff
    ROS_INFO("Calling Takeoff");
    crazyswarm::Takeoff takeoffCommand;
    takeoffCommand.request.groupMask = 0;
    takeoffCommand.request.height = 1.0;
    takeoffCommand.request.duration = ros::Duration(2.5);
    takeoffClient.call(takeoffCommand);

    //Sleep
    ROS_INFO("Sleeping");
    ros::Duration(5.0).sleep();
    
    //Call Land
    ROS_INFO("Calling Land");
    crazyswarm::Land landCommand;
    landCommand.request.groupMask = 0;
    landCommand.request.height =0.4;
    landCommand.request.duration = ros::Duration(2.5);
    landClient.call(landCommand);

    while (ros::ok()) {
        ROS_INFO("I'm finished");
        loop_rate.sleep();
    }
}