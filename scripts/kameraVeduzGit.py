#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 13:57:48 2024

@author: alperen
"""

#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class HedefeGit():
    def __init__(self):
        rospy.init_node("duz_git")
        self.hedef_konum = 5.0
        self.guncel_konum = 0.0
        self.kontrol = True
        rospy.Subscriber("odom",Odometry,self.odomCallback)
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz_mesaji = Twist()
        self.rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.kontrol:
                self.hiz_mesaji.linear.x = 0.5
                self.pub.publish(self.hiz_mesaji)
            else:
                self.hiz_mesaji.linear.x = 0.0
                self.pub.publish(self.hiz_mesaji)
                rospy.loginfo("hedefe varıldı!!")
            self.rate.sleep()

    def odomCallback(self,mesaj):
        self.guncel_konum = mesaj.pose.pose.position.x
        if self.guncel_konum <= self.hedef_konum:
            self.kontrol = True
        else:
            self.kontrol = False

class Kamera():
    def __init__(self):
        rospy.init_node("kamera_dugumu")
        self.bridge = CvBridge()
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        rospy.spin()
        
    def kameraCallback(self,mesaj):
        img = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")
        cv2.imshow("Robot Kamerası",img)
        cv2.waitKey(1)

if __name__ == "__main__":
    try:
        hedef_git = HedefeGit()
    except rospy.ROSInterruptException:
        print("düğüm sonlandı!!")

    try:
        kamera = Kamera()
    except rospy.ROSInterruptException:
        print("düğüm sonlandı!!")
