#!/usr/bin/env python
# coding: utf-8

# #            FOR LOOPS




x=[12,3,11]
   





print(x[0])





print(x[0],x[1])




for i in range(1,12):
    print(i)





for i in range(1,20,2) :  
    print(i)





sum=0
for i in range (1,5):
    sum=sum+i
    print(sum)



sum=0
for i in range (1,5):
    if i%2==0:
     sum=sum+i
    print(sum)




n=int(input("enter number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()





r=int(input("entre r "))
c=int(input("entre c "))
x=[]
val=[]
for i in range(0,r):
    for j in range(0,c):
            val.insert(j,input("entre %d %d elements " %(i,j)))
    x.insert(i,val)
    val=[]
y=[] 
for i in range (0,r):
      for j in range(0,c):
            val.insert(j,input("entre %d %d elements " %(i,j)))
      y.insert(i,val)
      val=[]
sum=[]
for i in range (0,r):
    for j in range(0,c):
            val.insert(j,x[i][j]+y[i][j])
    sum.insert(i,val)
    val=[]
print(sum)  


# # GOOD LUCK
# Abdulrahman Mohammed
