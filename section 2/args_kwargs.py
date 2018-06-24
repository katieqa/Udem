def my_method(arg1, arg2):
    return arg1 + arg2

my_method(5,6)

def my_long_method(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

def my_list_addition(list_arg):
    return sum(list_arg)

my_long_method(1,2,3,4,5)

my_list_addition([1,2,3,4,5])

def addition_simplified(*args):
    return sum(args)

addition_simplified(3,4,5,7,12) #gets passed in as a list, but unlimited number of arguments

##

def what_are_kwargs(*args, **kwargs):
    print(args)  #returns a tuple ()
    print(kwargs) #returns a set/dictionary {}

what_are_kwargs(12,34,56, name='Jose', location='UK')
#(12, 34, 56)
#{'name': 'Jose', 'location': 'UK'}

#arguments that are key:value pairs must come at the end

