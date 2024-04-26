#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:13:18 2024

@author: alperen
"""

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class LazerVerisi():
    def __init__(self):
        rospy.init_node("lazer_dugumu")
        rospy.Subscriber("scan", LaserScan, self.lazerCallback)
        self.pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.hiz_mesaji = Twist()
        rospy.spin()
   
    def lazerCallback(self, mesaj):
        sol_on = list(mesaj.ranges[0:9])
        sag_on = list(mesaj.ranges[350:359])
        on = sol_on + sag_on
        sol = list(mesaj.ranges[80:100])
        sag = list(mesaj.ranges[260:280])
        arka = list(mesaj.ranges[170:190])
        min_on = min(on)
        min_sol = min(sol)
        min_sag = min(sag)
        min_arka = min(arka)
        print(min_on, min_sol, min_sag, min_arka)
        if min_on < 1.0 or min_sol < 1.0 or min_sag < 1.0 or min_arka < 1.0:
            self.hiz_mesaji.linear.x = 0.1   # Hızı Sıfır yaparsak sürekli dönüyor.
            self.hiz_mesaji.angular.z = 0.5  # Dönüş hızı
            
        else:
            self.hiz_mesaji.linear.x = 0.25
            self.hiz_mesaji.angular.z = 0.0  # Dönüş yok
        self.pub.publish(self.hiz_mesaji)
            
if __name__ == "__main__":
    nesne = LazerVerisi()
