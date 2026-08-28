#String


rahul="rahul sah "
print(rahul)


first_rahul=rahul[0]
print(first_rahul)

slice_sah=rahul[0:5]
print(slice_sah)

num_list="0123456789"
print(num_list[:])#give all number
print(num_list[3:])#start from index 3 to end 
print(num_list[:7])#start from index 0 to end before 7 


print(num_list[0:7:2])#hoping by 1 number from 0 to 6
print(num_list[0:7:3])#hoping by 3 number from 0 to 6




print(rahul.lower())
print(rahul.upper())



sah= "    hello    "
print(sah)
print(sah.strip())#cancel space 


print(rahul.replace("rahul","swashank"))

rahul= "rahul, swas, me, him"
print(rahul.split(", "))


rahul = "rahul sah"
print(rahul.find("sah"))#from which index sah start
print(rahul.find("him"))#it will return -1 if it cannot find anything

rahul="rahul sah sah sah "
print(rahul.count("sah"))##it will return count of that string





food = "momo"
quantity=3
order = "I ordered {} plate of {} chicken "
print(order.format(quantity,food))# first replace by quantity and 3nd by food



#string to list : by using .join

chai_variety=["lemon","masala","ginger"]
print(", ".join(chai_variety))
print(" ".join(chai_variety))
print("/ ".join(chai_variety))



#length of string
rahul= "rahul sah"
print(len(rahul))


#return all letter of the string
for letter in rahul:
        print(letter)



#path
he="he said, \"rahul is nice guy\""
print(he)



rahul="rahul\nsah"
print(rahul)



 
rahul=r"rahul\nsah"
print(rahul)

