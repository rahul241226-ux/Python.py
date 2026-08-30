username  = "rahulsah"

def func():
    username= "rahul"
    print(username)


print(username)
func()

#if we comment out username in function then print search for upside and print rahulsah








#function2

x= 99#global declaration
def func2(y):
    z = x+y# if x is not in function then it will take the value of x from global declaration
    return z

result = func2(1)
print(result) 







#function3

x= 87
def fun3():
    global x
    x= 12
  
fun3()
print(x)






#function1


def f1():
    x =88
    def f2():
        print(x)
    f2()
f1()
