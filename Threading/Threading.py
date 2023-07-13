#!/usr/bin/env python
# coding: utf-8


# # Threading



from threading import *
def show():
    print("child thread")
t=Thread(target=show())
t.start()
print("parent thread")




from threading import *

class MyThread ():
    def run(self):
        for i in range (5):
            print("child class")
t=MyThread()
t.run()
for i in range (5):
            print("main thread")


# # multithreading



from threading import *
import time
class demo():
    def num(self):
        for i in range (1,6):
             print (" number is ", i)
             time.sleep(1) 
    def double(self):
         for i in range (1,6):
                print(" double number is ", i)
                time.sleep(1) 
    def square(self):
         for i in range (1,6):
                print(" the square number is ", i)
                time.sleep(1) 
obj=demo()
t1=Thread(target=obj.num)
t2=Thread(target=obj.double)
t3=Thread(target=obj.square)

t1.start()
time.sleep(0.2) 
t2.start()
time.sleep(0.2) 
t3.start()

t1.join()
t2.join()
t3.join()

print("main thread")


# # Created by
# Abdulrahman Mohammed
