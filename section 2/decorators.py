#@classmethod
#@staticmethod
#function that gets called before another function

import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I am the function now")

#my_function()

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("in the decorator!")
            if number == 56:
                print("not running function")
            else:
                func(*args, **kwargs)
            print("after the decorator")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_too(x,y):
    print("Hello")

my_function_too(57, 67)
