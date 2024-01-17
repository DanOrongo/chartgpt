# returning many no. of diff types using one function
def many_types(x):
    if x < 0:
        return 'Hello'
    else:
        return 0
    
# printing the function
print(many_types(5))
print(many_types(-8))


#a function without return statement will return none
def do_nothing():
    pass

print(do_nothing())


#prompting for arbitrary no. of arguments
def func(*args):
    for i in args:
        print(i)
        
func(1,2,3)

#prompting for abitrary no. of keyword arguments        
def func(**kwargs):
    for name, value in kwargs.items():
        print(name, value)
        
func(value1=1, value2=2,value3=3)

#calling with a dictionary
my_dict = {'foo':3, 'bar':2}
func(**my_dict)



def func(arg1, arg2=10, **kwargs):
    try:
        kwarg1 = kwargs.pop('kwarg1')
    except KeyError:
        raise TypeError("missing required keyword-only argument: 'kwarg1'")
    
    kwargs2 = kwargs.pop('kwarg2', 2)                        




#prompting for lambda function
greet_me = lambda: "Hello"
print(greet_me())

strip_and_upper_case = lambda s:s.strip().upper()
strip_and_upper_case("   hello  ")

#taking arbitrary number of arguments using lambda
greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='Dan')

#with numerical lists
my_list = [3, -4, -2, 5, 1, 7]
sorted(my_list, key=lambda x: abs(x))


#calling functions from inside a lambda function
def foo(msg):
    print(msg)
    
greet = lambda x = "hello world": foo(x)
greet()

#defining function with optional argument
def make(action= 'nothing'):
    return action

make("fun")


#optional mutable arguments
def f(a, b=42, c=[]):
    pass

print(f.__defaults__)



def append(elem, to=[]):
    to.append(elem)
    return to

append(1)
append(2)
append(3, [])
append(4)


def append(elem, to= None):
    if to is None:
        to = []
        
    to.append(elem)
    return to

#argument passing and mutability
def foo(x):
    x[0] = 9
    print(x)
    
y = [4,5,6]
foo(y)
print(y)

def foo(x):
    x[0] = 9
    x = [1,2,3]
    x[2] = 8
    
y = [4,5,6]
foo(y)

x = [3,1,9]
y = x.append(5)
x.sort()
x = x +[4]
z = x 
x += [6]
x = sorted(x)


#returning values fro functions
def give_me_five():
    return 5

print(give_me_five())

#returning multiple values
def give_me_two_fives():
    return 5,5

first, second = give_me_two_fives()
print(first)
print(second)


#closure
def makeInc(x):
    def inc(y):
        return y + x
    return inc

incOne = makeInc(1)
incFive = makeInc(5)

incOne(5)
incFive(5)