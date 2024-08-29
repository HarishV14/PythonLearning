def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

def sub(x,y):
    return x-y

resultAdd = calculate(add, 4, 6)
resultSub = calculate(sub, 6, 4)
print(resultAdd)  # prints 10
print(resultSub)  # prints 10

print("----------------------------------------------------------------")

def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    func()
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()

print("----------------------------------------------------------------")


def make_pretty(func):

    def wrapper(a):
        print("I got decorated 2")
        func(a*10)
        # return func
    return wrapper

@make_pretty
def ordinary(val):
    print("I am ordinary ",val)

ordinary(20)  

print("----------------------------------------------------------------")

#using paramenters
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)

print("----------------------------------------------------------------")
def star(func):
    def inner(*args):
        print("*" * 15)
        func(*args)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args):
        print("%" * 15)
        func(*args)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("hel")

#ABOVE is equals to printer = star(percent(printer))    

print("------------------------------------------------")
p=star(printer)
p("hell0")

p1=percent(printer)
p1("welcome")

print("----------------------------------------------------------------")
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        print(lie)
        lie = lie - 3 # very friendly, decrease age even more :-)
        return method_to_decorate(self, lie)
    return wrapper
    
    
class Lucy(object):
    
    def __init__(self):
        self.age = 32
    
    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I am {0}, what did you think?".format(self.age + lie))
        
l = Lucy()
l.sayYourAge(4)

print("----------------------------------------------------------------")

def names(n1,n2):
    def check(func):
        def wrapper(*args):
            print(n1,n2)
            func(*args)
        return wrapper
    return check

@names("harish","deepak")
def display(a,b):
    print(a,b)

display("welcome","hello")