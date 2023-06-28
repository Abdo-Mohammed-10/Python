#!/usr/bin/env python
# coding: utf-8

# #                                        SETS



x=(['2','3','66'])
s=set([1,2,3,4])
print(type(x))
print(type(s))    # NOTE METHODE X =! METHODE S 




s.add(33)
# x.add(15) not true
print(x)
print(s)




f=frozenset([1,5,6,4]) #note frozenset U cannot add any elements
print(f)




x=set(['d','a','x'])
y=set(['d','a','v'])
print(x.union(y))
print(x.difference(y))


# # GOOD LUCK
# created by Abdulrahman Mohammed
