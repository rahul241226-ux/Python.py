#Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.



order_size= str(input("enter the size of coffee:"))
extra_shot = True

if extra_shot:
    coffee= order_size+"_coffe with an extra shot of espresso"
    print(coffee)

else:
    coffee= order_size+"_coffe with an extra shot 0f espresso"
    print(coffee)
    