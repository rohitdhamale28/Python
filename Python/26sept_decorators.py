# variable Scope 


def f1(x):
    print(x)
    x=x+1              # this will give error as 'x' is a global variable and the function trying to modify a global variable 
    
x=100
print(x)
f1(x)

#==============================================================================

def f1():
    global count  # global keyword to access global variable 
    count+=1
    x=20
    print(x)
# this will print x= 20 as x is a local variable of f1

x=100
count =0
print(x) #100
print(count) #0
f1()
print(x) #100
print(count) #1   functon f1 modifies count , using global count 


#===================================================================================

##### Generator Function ####

def mynumbers():
    yield 1    # yield is used instead of return , yield 1 val at a time and yeild remembers the last returned value.
    yield 2    # n when next is called , next yield val is returned 
    yield 3
    yield 4
    yield 5
    
#e.g. Range is a generator function

def mynumbers1():
    for i in range(1,6):
        yield 1
        
for i in mynumbers():
    print(i)
    
print(mynumbers1()) # <generator object mynumbers1 at 0x75ca5f5381e0>
# this print generatro object not value

g = mynumbers()
print(type(g)) #O/P  <class 'generator'>
print(next(g)) #op : 1   "use next function to get the next value"
print(next(g)) #op : 2


"""we can now print(generator function), it will return an object. 
to print all the generated value, use it inside for loop or manually type next"""
# print(mynumbers())   #this will give object!


# the below code will read one line from the file at a time and remember it.
def myf1():
    with open("employeeinfo.txt") as fh:
        for ln in fh:
            yield ln


# Generator functions are used in web scrapping code


#===================================================================================

# DECORATORS (e.g., @abstractmethod, @staticmethod)

"""
Decorators allow you to execute actions before and after a defined method 
without changing its core logic. They reduce code duplication when multiple 
functions require the same pre- or post-processing tasks.

"""

def logging():
    print("in logging function")
    
def validate_usr():
    print("in validate user")
    

def mydecorator(f):  # 'f' is the target function being decorated
    def inner_function(*args, **kwargs):  # Wraps 'f' and accepts any positional/keyword arguments
        logging()               # Executed first
        validate_usr()          # Executed second
        print("in mydecorator") # Executed third
        print("-" * 80)
        
        z = f(*args, **kwargs)  # Calls the original function and stores its return value
        
        print("exiting from mydecorator")
        return z                # Returns the result back to the original caller
    return inner_function
    

@mydecorator  # Equivalent to: f1 = mydecorator(f1)
def f1(x, y, **kw):
    print("in f1()", x, y, kw)
    return x + 10

@mydecorator  # Equivalent to: f2 = mydecorator(f2)
def f2():
    print("in f2()")
    

print(f1(10, 20, a=34, b=35))
f2()




