


#LISTS 
    #                                  ----> using []




# Creating list 




x=[1,36,1,2,5,1,16,22,33]
b=[1,36,1,2,5,"sss"]
y=[12,2,5,33,1,1]
z=['DS','SS','FF']
d=[[1,6,5],["ss","cc","vv"]]
print(d)
print(b)




# Accessing lists




print(x[0]) 
print(y[2])
print(z[2])
print(d[0])
print(d[1])




x[:3] #x=[1,36,1,2,5,1,16,22,33]




y[2:] #y=[12,2,5,33,1,1]




z[0:2] #z=['DS','SS','FF']




print(x+y)
print(x+z)
# (+) only arthimitic can U use it .




del(x[0]) #--->> delete index 0
# x=[(1),36,1,2,5,1,16,22,33]




print(x)




print(x[-2]) # print second element from last
print(x[-3]) # print third element from last
# x=[36, 1, 2, 5, 1, 16, 22, 33]




x[::-1] # flip list from last to first .




print(x[::2]) #--->skip an element
print(x[::3]) #--->skip 2 elements
print(x[::4]) #---> skip 3 elements
print(x[::-2])#---> skip an element from last
# x=[36, 1, 2, 5, 1, 16, 22, 33]




# Operating on list




z=[1]*3 # create list all element will be 1 .
print(z)
y=[5]*4 # create list all element will be 5 .
print(y)




list("abdo")




x




t , *others=x
print(t) # print first element  
print(others)




x




len(x)




print(min(x))
print(max(x))
print(sum(x))
print(sum(x)/len(x))




# METHODS OF LISTS




f=[55,6,6,1]




z=[1,2,'dd',66]




z.append(44) # -->> add 44 at last
print(z)




f.extend(z) # add list z to f
print(f)




f.insert(0,'abdo')
print(f)




f.remove(6)# remove ==== pass the elements not index 
f.remove('dd')




print(f)




del(f[0])




f




c=['s','v','f']
c.sort() # sort----->>> arrange the elements




print(c)




d=[15,36,2]
d.sort()




print(d)




# GOOOOOOOOD LUCK
                                   # Created by Abdulrahman Mohammed                 

