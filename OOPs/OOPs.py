#!/usr/bin/env python
# coding: utf-8

# # OOPs



class car():
    def __init__(self,year,speed):
        self.year=year
        self.speed=speed
    def getspeed(self):
        print(" speed is ",self.speed, "mph" )
    def setspeed(self,speed):
        self.speed=speed




Audi=car(1908,166)
Ford=car(1988,140)




Audi.getspeed()
Ford.getspeed()




Audi.setspeed(200)
Ford.setspeed(150)




Audi.getspeed()
Ford.getspeed()


# # GOOD LUCK
# Abdulrahman Mohammed
