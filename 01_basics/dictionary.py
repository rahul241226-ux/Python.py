types= {"momo": "chicken","drink":"coco cola", "egg":"duck"}


print(types)
print(types["momo"])
print(types.get("drink"))


#replace
types["egg"]="fresh"
print(types)



#iteration
for food in types:
        print(food)
#for food in types:
 #       print(food,types[food])
for key , values in types.items():
        print(key,values)



if "egg" in types:
        print("I have eggs ")
        print(len(types))

#adding new items 
types["game"]="football"
for key , values in types.items():
        print(key,values)


#deleting items 
types.pop("egg")
for key , values in types.items():
        print(key,values)




#deleting last items
types.popitem()
print(types)


#deleting any particular item
del types["momo"]
print(types)



#copying
types_copy=types.copy()
print(types_copy)





#loop
tea_shop={

"chai":{"masala":"spicy","ginger":"zesty"},
"tea":{"green":"mild","black":"strong"},
        
}
print(tea_shop)
print(tea_shop["chai"]["ginger"])






#square number

squared_num={x:x**2 for x in range (6)}
print(squared_num)


squared_num.clear()
print(squared_num)



#adding values to individual keys
keys=["masala", "ginger", "lemon"]
print(keys)


default_value="Delicious"
new_dict= dict.fromkeys(keys, default_value)
print(new_dict)