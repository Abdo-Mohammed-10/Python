#!/usr/bin/env python
# coding: utf-8

# # While loops


i=5
while i<=10:
    print ("simplelearn : ",i)
    i+=1




i=1
sum=0
while i<=10:
    sum=sum+i
    i+=1
print(sum)




i=1
sum=0
while i<=10:
    if i%2==0 :
         sum=sum+i
    i+=1
print(sum)


# # FLIP NUMBERS



n=int(input("entre a number : "))
nr=0
while n%10!=0 :
    c=n%10
    nr=nr*10+c
    n=n//10
print(nr)


# # TRY & EXCEPT



X=[1,2,3,"SIMPLElearn"]
length=0
i=0
try:
     while X[i] :
        length+=1
        i+=1
except IndexError :
    print(length)




n=int(input("entre a number "))
i=1
while i<=n:
    j=1
    while j<=i :
        print (i,end=' ')
        j+=1
    i+=1
    print()




import random
nump= random.randint(1000,9999)
print(nump)
n=int(input("entre 4 digit "))
while n!=10:
    num=nump
    cor=0
    while num%10:
        numc=num%10
        nc=n%10
        num=num//10
        n=n//10
        if numc==nc:
            cor=cor+1
        if cor==4:
            print("excllent you guessed it right ")
            break
        else :
            print( "%d digit were guessed right"%cor)
            n=int(input("entre a 4 digit number"))
    else:
        print("you quite the game")
    break
