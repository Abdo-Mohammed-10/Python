#!/usr/bin/env python
# coding: utf-8

# # ______________________________  loops    __________________________________

# #                                          while_loop



val=int(input("entre nmber "))
while val%2 !=0 :
    val=int(input("entre nmber "))
else:
        print("even")


# #                                 for loop



x=[1,3,6,"ss"]
for i in x: # (i in x ) : mean counter count index and print his values
    print(i)




x="sam"
for i in x :
    print(i)


# #                               Nested_loop



x=[[1,2,3],[3,6,6]]
for i in x :
    print(i)




x=[[1,2,3],[3,6,6]]
for i in x :
    for j in i:
        print(j)




x=[[1,2,3],[3,6,6]]
for i in x :
    for j in i:
        print(j,end="")
        print()


# #                 control of loop (BREAK & CONTINUE)
# 

# # break



x="abdo mohammed"
for i in x :
    print(i)
    if i=="d":
         break
         print(i,end="")


# #                          continous



for i in [1,23,5,3] :
 if i>10:
     continue
 print(i)
else:
    
    print("not")


# # GOOOOOOOOD LUCK
# Abdulrahman Mohammed
