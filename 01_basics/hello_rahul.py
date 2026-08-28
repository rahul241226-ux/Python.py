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



#we can als0 import math
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









#3. List or Array

my_list = [1, 2, 3, 4, 5]
print("Length of my_list:", len(my_list))







#4.Dictionary: it is a collection of key value pairs, in {}

my_dict = {"name": "Rahul", "age": 25, "city": "New York"}# there is key and value pair in dictionary 

print("Length of my_dict:", len(my_dict))
print("Length of my_dict:", my_dict["name"])
print("Length of my_dict:", my_dict["age"])
print("Length of my_dict:", my_dict["city"])
#print("Length of my_dict:", my_dict["intrest"])








#5. tuple: it is a collection of ordered and immutable elements 

my_tuple =(1,2,3,4,5)
print("value at index 0 :",my_tuple[0])
print("value at index 0 :",len(my_tuple))










#internal working in python 

x=3
x='rahul and code'
x=3.23
print("value of x :",x)



x = 5
y=9
x=x+3
print("value of x :",x)#here x is mutable so it assigned 8


y=x+9
print("value of y :",y)



my_listone=[1,2,3,4,5]
my_listtwo=my_listone
print("my_listone:", my_listone)
print("my_listtwo:", my_listtwo)



l1= [1,2,3]
l2=l1
print("l1:", l1)
print("l2:", l2)
l1[0]=33
print("l1:", l1)
print("l2:", l2)






c1=[1,2,3,4]
c2=c1
c2=[5,6,7,8]
c1[1]=8
print("c1:", c1)
print("c2:", c2)


import copy
c2=copy.deepcopy(c1)
print("c2:", c2)



n= [1,2,3]
m= n
print(m==n)


m is n 
print(m is n )

#let 
m = [1,2,3]#it is different object in memory 
m==n
print(m==n)

m is n 
print(m is n )







#Numbers in python


x= 2
y=3
z=4
print("add of x and y:", x+y)
print("add of x and y and multi z:", (x+y)*z)
print("add of x and y:", 40.4+2.4)
print("add of x and y:", int(40.4+2.4))
print("add of x and y:", float(40.4+2.4))
print("add of x and y:", 'rahul'+'sah')


print("add of x with 1  and y with 1:",x+1,y+1)
print("power of z is 2:", z**2)
print("power of 2 is 1000:", 2**1000)#py can handel much higher byte

print("reper:",repr('rahul'))
print("string:",str('rahul'))
print("print:",'rahul')



print(1== 2 < 3)





import math 
print(math.floor(3.5))#to lower value
print(math.floor(-3.5))
print(math.trunc(3.5))#towards zero
print(math.trunc(-3.5))


#complex number in python
print(2+3j)
print((2+3j)*3)


#octals 
print(0o10)
print(oct(64))


#hexal
print(0x10)
print(hex(16))


#binary 
print(0b1000)
print(bin(8))




#conversion from int to oct,hex,binary
print(int('64',8))
print(int('64',16))
print(int('10000',2))





#left shift
x=1
print(x<<2)




#right shift
x=1
print(x>>2)



import random
print("random number between 1 and 10:",random.randint(1,10))

l1=['A','B','C','D','E','F','G','H','I']
print("random choice from l1:",random.choice(l1))


l2=['rahul','raja','dev','aadi','raju']
random.shuffle(l2)
print("random suffle from l1:",l2)




#we can import decimal
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')-Decimal('0.4'))


#we can import fraction
from fractions import Fraction
myfra=Fraction(2,7)
print(myfra)





#SETS

setone={1,2,3,4}
intersection=setone & {1,3}
print(intersection)

setone={1,2,3,4}
union=setone | {1,8,9}
print(union)




#Bollean

print(True==1)
print(False==1)

print(True + 4)#True is equal to 1
print(False + 4)#False is equal to 0
