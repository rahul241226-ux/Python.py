#Problem: Given a list of numbers, count how many are positive.


numbers =[1,-2,3,-6,4,33,-9,10]
positive_number_count=0
for num in numbers:
    if num >0:
        positive_number_count = positive_number_count+1
print("final count of positive number:", positive_number_count)
