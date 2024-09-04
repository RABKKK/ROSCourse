#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import time
import math

class ReadSensor():

    def __init__(self, robot_name="turtlebot"):
        rospy.init_node('scanner_measurement_node', anonymous=True)

        rospy.loginfo("Hokuyo Scanner using hokuyo_node...")      
  
        self._check_laser_ready()


        self.laser_subscriber = rospy.Subscriber(
            '/scan', LaserScan, self.laser_callback)
        
        self.ctrl_c = False
        self.rate = rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)

	    
    def _check_laser_ready(self):
        self.laser_msg = None
        rospy.loginfo("Checking Laser...")
        while self.laser_msg is None and not rospy.is_shutdown():
            try:
                self.laser_msg = rospy.wait_for_message("/scan", LaserScan, timeout=1.0)
                rospy.logdebug("Current /scan READY=>" + str(self.laser_msg))

            except:
                rospy.logerr("Current /scan not ready yet, retrying for getting scan")                
        rospy.loginfo("Checking Laser...DONE")
        return self.laser_msg

    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True

    def laser_callback(self, msg):
        self.laser_msg = msg

    def summit_laser_callback(self, msg):
        self.summit_laser_msg = msg

    def get_laser(self, pos):
        time.sleep(1)
        return self.laser_msg.ranges[pos]


    def get_laser_full(self):
        time.sleep(1)
        return self.laser_msg.ranges
        
    def filter_datinrang(self, xyrange):

        return [self.xy,self.mean]  




if __name__ == '__main__':
    
    robotcontrol_object = RobotControl()
    try:
        robotcontrol_object.move_straight()

    except rospy.ROSInterruptException:
        pass
