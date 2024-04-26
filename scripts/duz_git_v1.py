#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 2 10:17:39 2024

@author: alperen
"""
import rospy
from geometry_msgs.msg import Twist

def hareket():
    rospy.init_node("duz_git")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    hiz_mesaji = Twist()
    hiz_mesaji.linear.x = 0.5
    
    mesafe = 5
    yer_degistirme_x = 0
    t0 = rospy.Time.now().to_sec()
    while(yer_degistirme_x < mesafe ):
        pub.publish(hiz_mesaji)
        t1 = rospy.Time.now().to_sec()
        delta_t = t1 - t0
        yer_degistirme_x = hiz_mesaji.linear.x * delta_t
        rospy.sleep(0.1)  
        
    hiz_mesaji.linear.x = 0.0
    pub.publish(hiz_mesaji)
    rospy.loginfo("Hedefe varıldı!!!")

hareket()

