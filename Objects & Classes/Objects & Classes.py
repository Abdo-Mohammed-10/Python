#!/usr/bin/env python
# coding: utf-8

# # Objects & Classes



class person :
    def __init__(self):
        self.name="sam"
        self.gender="male"
        self.age=22
    def talk(self):
        print("my name", self.name)
    def vote(self):
        if self.age<18:
            print("i am not eligable to vote")
        else:
            print("i am eligable to vote")
    




obj= person()
obj.talk()
obj.vote()




class person :
    def __init__(self,n,g,a):
        self.name=n
        self.gender=g
        self.age=a
    def talk(self):
        print("my name", self.name)
    def vote(self):
        if self.age<18:
            print("i am not eligable to vote")
        else:
            print("i am eligable to vote")
    




obj2=person("quarisma","male",22)
obj3=person("Anne","female",16)
print(obj3.name,obj2.name)




obj2.talk()
obj2.vote()




obj3.talk()
obj3.vote()


# # Good luck
# Abdulrahman Mohammed
