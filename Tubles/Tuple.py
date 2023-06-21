# #                                         python tuples
#                                    using parentheses () or not 

# #                                         creating tuples



emp=()
print(type(emp))




city="abdo",
# note comma ( , )  make variable his type tuble .
c="d"
print(type(c))
print(type(city))




city=("a","b")
type(city)




print(type(city))




city




city=15,16 # note that 
print(type(city))


# #                             Accesing



city[1]




city[0]




city[0]-city[1]




#city.append("am") # U cannot use append with tuples


# #                               concatenation



c=(1,2,3,5)
a=("ab","as","cc","vc")
print(c+a) # only arthimitic u can use it with tuples 


# #                                    NESTING
#              nesting in tuble mean make in side tuble many tubles



nest=(c,a)
print(nest)


# #                                        Repetition 



rep=("p")*5
print(rep)



rep="c"*5
print(rep)




rep=("gg",)
print(rep*3)




print(rep) # print the last value are stored in rep --->> "gg", 


# #                                            slicing



n=(1,2,3,6,5,88)
n[1::]




n[1:]




n[::-1] # ---> flip




n*3


# # Unpacking



tuple("simple")




num=(2,5,6,9)
a,b,c,d=num
print(a,b,c,d)




*a,b,c=num    # ---->> here make elements (a and b) in side list and other element print them normaly
print(a,b,c)        # i mean make the element and the element after it in side list




a,*b,c=num   #----->> # ---->> here make elements (b and c)in side list and other element print them normaly
print(a,b,c)


# #                                           deleting tuples



t=(1,2,3)
t




del t


# In[42]:


# print(t) # after del the tuple not defined and u cannot ----->> print it so you will see error 


# #                                       built in function



c=(1,2,3,6,5,5)
c.count(5)




sum(c)




len(c) 




max(c)




min(c)


# # Converting list to tuple 


lis1=[5,6,"gg"]




b=tuple(lis1)




print(type(b))




print(type(lis1))


# # Nesting tuples in a list 



lst=[(1,2,5),(6,9,4,5)]




print(lst)




lst.append(("dd","ck","ddo"))




print(lst)




lst.remove((1, 2, 5))




print(lst)


# # Nesting lists within tuple



tp=(['a','b','c'],['c',15,36])




print(tp)




tp[0].append('z')




print(tp)




tp[0].remove('c')




print(tp)




# tp.append(['d',5,6]) # --->> U CAN'T append in tuple


# #                                        GOOOOOOD LUCK
#                     created by Abdulrahman Mohammed  💕❤️
