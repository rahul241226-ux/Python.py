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
        print(x)#it will search for x in f1 and if there is no x then it will find abobe it
    f2()
f1()



#closure in py 



def f1():
    x =88
    def f2():
        print(x)
    return f2
myresult = f1()
myresult()





#new 

def rahul(num):
    def actual(x):
        return x ** num
    return actual



f = rahul(2)
g = rahul(3)

print(f(3))
print(g(3))