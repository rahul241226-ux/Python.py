#Problem 2: Debugging Function Calls

#Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.


# def debug(func):
#     def wrapper(*args, **kwargs):#wrapper function takes any number of positional and keyword argumrnt
#         print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @debug
# def example_function(x, y):
#     return x + y

# example_function(3, 4)








def dubug(func):
    def wrapper(*args, **kwargs):
        args_value =', '.join(str(arg) for arg in args)
        kwargs_value =', '.join(f"{k}={v}"for k, v in kwargs.items())
        print(f"Calling {func.__name__} with arguments: {args_value}, {kwargs}")
        return func(*args, **kwargs)

    return wrapper

@dubug
def hello():
    print("hello world")

@dubug
def greet (name, greeting="hello"):
    print(f"{greeting},{name}!")


hello()
greet("rahul", greeting="hi")