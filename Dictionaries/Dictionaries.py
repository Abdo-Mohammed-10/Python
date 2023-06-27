#!/usr/bin/env python
# coding: utf-8

# #                                           DICTIONARIES



d={} # equal to f=dict({})  or f=dict([()])
print(type(d))


# # Creating dict



d={1:"abdo",2:"mohammed"}




type(d)




print(d)




print(d[1]) # --->> here pass key


# # Nested dict



f={1:{"abdo","c"},2:"mohammed"}




print(f)


# #                                          adding elements



d={}
d[0]="ab"
d[1]="gg"
print(d)




d={}
print(d)



d["omar"]="ben-khatab"
print(d)




d["name"]={"alhabib":"mohammed","rasulallah":"mohammed"}




print (d)




print(d["name"]["rasulallah"])


# #                                      accessing elements



print(d.get('omar')) #{'omar': 'ben-khatab', 'name': {'abdullah': 'mohammed', 'rasulallah': 'mohammed'}}


# #                                        deleting dict



d.pop('omar')  # with function pop pass -->> key or dict




print(d)




d.popitem() # delete last elements




print(d)


# #                                        USING IN BUILT FUNCTION



d={0:"bbb",1:"ddd",2:"sss"}




print(d.values()) # just value only




k={"cc","xx","zz"}
val=1
print(dict.fromkeys(k,val)) # fromkeys set every elements of k as key and and his value will be val .
print(k)



k.clear()




print(k)


# #                                 GOOOOOOOD LUCK 
#  Abdulrahman Mohammed
