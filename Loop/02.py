#Problem: Calculate the sum of even numbers up to a given number n.


number =[1,3,4,5,6,7,8,9,10]
sum = 0;

for num in number:
    if num % 2 == 0:
        sum = sum + num;

print("sum of given all even number :", sum)