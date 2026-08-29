#Problem: Compute the factorial of a number using a while loop.



number = int(input("Enter the number:"))
factorial = 1

while number >=1:
    
    factorial= factorial*number
    number = number- 1

print("factorial of giver number:", factorial)