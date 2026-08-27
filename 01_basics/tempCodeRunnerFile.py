print("hello Rahul")




def rahul(n):
    print(n)

rahul(9)



for r in "rahulsah":
    print(r);




#immutable and muttable

x=10

y=x
print("x:",x)
print("y:",y)



x=20
print("x:",x)
print("y:",y)# y does not change because it is immutable;



#Data types in python 

#1.Numbers
x= 12+12
y=2.5*5
z=2** 300 # power of 2 is 300

print("x:",x)
print("y:",y)
print("z:",z)



#we can als import math
import math
p= math.pi
print("value of pi:",p)


#we can also import random

import random
r= random.choice([2,2,3,4,5,4,6,100]);
print("random number: ", r)





#2.String: immutable data type which cannot change once created
username= "rahulkumar"
print("Length of username:", len(username))
print("string of username:", username[2])
print("string of username:", username[-1])# it will start from end of the string

print("string of username:", username[1:3])# it will print from index 1 to 3 but not include 3

print("string of username:", username[0:7])






# List or Array

my_list = [1, 2, 3, 4, 5]
print("Length of my_list:", len(my_list))




#Dictionary: it is a collection of key value pairs, in {}

my_dict = {"name": "Rahul", "age": 25, "city": "New York"}# there is key and value pair in dictionary ..

print("Length of my_dict:", len(my_dict))
print("Length of my_dict:", my_dict["name"])
print("Length of my_dict:", my_dict["age"])
print("Length of my_dict:", my_dict["city"])
#print("Length of my_dict:", my_dict["intrest"])


#tuple: it is a collection of ordered and immutable elements 

my_tuple =(1,2,3,4,5)
print("value at index 0 :",my_tuple[0])
print("value at index 0 :",len(my_tuple))