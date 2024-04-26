#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:41:19 2024

@author: alperen
"""

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class HedefeGit():
    def __init__(self):
        rospy.init_node("duz_git")
        self.hedef_konum = 5.0
        self.guncel_konum = 0.0
        self.kontrol = True
        rospy.Subscriber("odom",Odometry,self.odomCallback)
        pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        hiz_mesaji = Twist()
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.kontrol:
                hiz_mesaji.linear.x =0.5
                pub.publish(hiz_mesaji)
            
            else:
                hiz_mesaji.linear.x = 0.0
                pub.publish(hiz_mesaji)
                rospy.loginfo("hedefe varıldı!!")    
            rate.sleep() 
        
    def odomCallback(self,mesaj):
        self.guncel_konum = mesaj.pose.pose.position.x
        if self.guncel_konum <= self.hedef_konum:
            self.kontrol = True
        else:
            self.kontrol = False
            
            
try:
    HedefeGit()            
        
except rospy.ROSInterruptException:
    print("dügüm sonlandı!!")        
        
        
        
        
        