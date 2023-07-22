#!/usr/bin/env python
# coding: utf-8

# # Inheritanc

# In[1]:


class car():
    def __init__(self,year,speed):
        self.year=year
        self.speed=speed
    def getspeed(self):
        print(" speed is ",self.speed, "mph" )
    def setspeed(self,speed):
        self.speed=speed


# In[7]:


BMW=car(2015,160)


# In[12]:


class sedan (car): # child class
    def accelerate(self):
        print('137')
    def opentrunk(self):
        print('trunk has been opened')
class suv(car): # child class
     def accelerate(self):
        print('100')
honda=sedan(2018,150)
BMW.getspeed()
honda.getspeed()
honda.opentrunk()
honda.accelerate()


# # Goood Luck
# Abdulrahman Mohammed
