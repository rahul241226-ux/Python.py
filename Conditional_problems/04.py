#problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)


fruit = "banana"
color= str(input("Enter the condition of fruit:"))

if fruit == "banana":
    if color=="green":
        print("unripe")
    elif color =="yellow":
        print("ripe")
    elif color == "brown":
        print("overripe")
