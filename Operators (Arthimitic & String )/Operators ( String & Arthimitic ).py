#!/usr/bin/env python
# coding: utf-8
                                    #Arthimitic operator
    #                                      (+,-,%,*)
x=66
y=12
result=x+y+22
print(x+y)
print(x-y)
print(x*y)
print(x^y)
print(x%y)
print(y%x)
#note: y%x != x%y
print(x/y)
print(x//y)
print(result)




#ARTHIMITIC WITH LISTS




x=[1,2,2]
y=[3,6,94]




print(x+y) #that is only  arthimtic operator true

# print(x-y) not true

# print(x*y) not true

# or print(x/y) too not true




print(x,y)
print(x[0]+y[1])
print(x[0]*y[2])   # Applying arthimitic operator just like that 




#ARTHIMITIC WITH TUPLES




x=(123,"ABF")
y=(33,25)




print(x+y)# (only)-->> Arthimitic true like lists .
print(x[0])




# pr(x-y) #and other arthimitic operator can't use it until "+"




print(x[0]+y[0])  # YOU CAN USE THE ARTHIMITIC OPERATOERS JUST LIKE THAT
# print(x[1]+y[1])  # note : impossible add int to ---> string , so you find errors




#ARTHIMITIC WITH SETS




x=set([1,2,"kk"])
y=set([22,"dd",55])
print(x,y)




# print(x+y) # ( YOU CAN'T USE ANY ARTHIMITIC OPERATORS) WITH SET
# print(x[0]+y[1]) # also like that




#                                         string operators 

x="my name"
y="abdulrahman"
print(x+y)
print(x[1])
print(x[1]+y[3])

print(x[1:5]) #count from index 1 to index 4 .
print(x[:5]) #count from index 0 to index 4 .
print(y[5:])  # Note : count from index (5) to index end .

print(len(x))
print(len(y))
# print(x-y) #thats not true 

#GOOD LUCK
     #                            created with Abdulrahaman Mohammed

