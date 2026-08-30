#Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def area_of_circle(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = area_of_circle(3)

print(f"Area of circle: {a:.2f}")
print(f"Circumference of circle: {c:.2f}")
