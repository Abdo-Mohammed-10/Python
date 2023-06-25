#!/usr/bin/env python
# coding: utf-8

# #                         STRINGS 



n="محمد صلى الله عليه وسلم"
for i in n :
    print(i)
    




print(type(n))




m='''abdo
mohammed '''  #---->> u can use three cotes instead of double cotes
print(m)
print(len(m))




print(m[:7])




print(m[2:7])




print(m[7:])




n="abdo mohammed"
print(n.upper())
print(n.lower())




print(n.find("b")) # is equal to print(n.index("b"))




print(n.index("b"))




print(n.split()) # or print(n.split(" "))




print(n.split(" "))




n.rpartition("e") #--->> 😂 وعزة جلالة الله الدالة دي ماعارف اشرحها بس فاهمها




print(n.replace("abdo","mohammed"))  # -->> n="abdo mohammed"
           #        1       2        
    
# replace mohammed instead of abdo 




x="abdo"
y="mohammed"
z=x+" "+y+" A"
print(z)




p="{},{}????".format(x,y)




print(p)


# #                          GOOOOOD LUCK
# created by Abdulrahman mohammed
