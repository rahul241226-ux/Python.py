#Problem: Given a string, find the first non-repeated character.


input_string = "nabin"




for char in input_string:
    #if input_string.count(char) == 2: for repeated string for 2 times , if we want to get string repeated for 3 times then change count as 3 ,
    if input_string.count(char) == 1:
        print("char is:", char)
        break# it is used so we does not need to go further after getting what we are seeking for and does not apply loop to all of them , it will give first unrepeated string but if we won't put break then we will get all unrepeacted strings