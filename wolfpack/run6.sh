#! /bin/bash

rosrun wolfpack cycleAssigner &
ROS_NAMESPACE=robot_0 rosrun wolfpack follower &
ROS_NAMESPACE=robot_1 rosrun wolfpack follower &
ROS_NAMESPACE=robot_2 rosrun wolfpack follower &
ROS_NAMESPACE=robot_3 rosrun wolfpack follower &
ROS_NAMESPACE=robot_4 rosrun wolfpack follower &
ROS_NAMESPACE=robot_5 rosrun wolfpack follower &
