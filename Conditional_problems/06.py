#Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance= int(input("enter the distance:"))

if distance <= 3:
    print("walk")
elif distance <=15:
    print("bike")

else :
    print("car")