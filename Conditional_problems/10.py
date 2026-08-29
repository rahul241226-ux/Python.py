#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).



pet = str(input("enter a species of pet:"))
age = int(input("enter the age of pet:"))


if pet == "dog" and age <2:
    print("Recommend a puppy food")

elif pet=="cat" and age >5:
    print("Recommend a senior cat food")

else:
    print("History of pet is in not in file")