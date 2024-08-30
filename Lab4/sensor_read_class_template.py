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
        self.xy=[[],[]]
        self.mean=[0,0]
        cnt=0        
        for i in range(len(self.laser_msg.ranges)):
          temp=[self.laser_msg.ranges[i]*math.cos(i*self.laser_msg.angle_increment), self.laser_msg.ranges[i]*math.sin(i*self.laser_msg.angle_increment)]
          if temp[0]>xyrange[0] and temp[0]<xyrange[1] and temp[1]>xyrange[2] and temp[1]<xyrange[3]:
            self.xy=[self.xy[0]+[temp[0]],self.xy[1]+[temp[1]]]
            self.mean=[self.mean[0]+temp[0],self.mean[1]+temp[1]]
            cnt+=1
        self.mean=[self.mean[0]/cnt,self.mean[1]/cnt]
        return [self.xy,self.mean]  
        
    #Step 0    
    #Define method to determine the data in the region of interest without 'Inf' etc and return it as a list
    #Declare variables to store the filtered data in the ROI
    
    #Step -1
    #Define method to return the mean of the filtered data 




