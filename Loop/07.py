#Problem: Keep asking the user for input until they enter a number between 1 and 10.



while True:
    number = int(input("Enter value between 1 and 10: "))
    if 1<= number <= 10:
        print("Got your number.")
        break
    else:
        print("not present.")