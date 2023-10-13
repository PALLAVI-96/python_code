#fnction inside function
def hello(name='jose'):
    print("the hello() functn has been executed")
    
    def greet():
        return "\t this is the greet function inide hello()"
    def welcome():
        return "\t this is the welcome functn inside hello()"
    #print(greet())  #greet and welcome can used only inside hello() function
    #print(welcome())
    if name=='jose':
        return greet()
    else:
        return welcome()
        
x=hello()
print(x)

#functn inside functn

def cool():
    def super_cool():
        return 'i am very cool'
    return super_cool
some=cool()
print(some())


#passing function as argument

def hai():
    return 'Hi rose!'

def other(func):
    print('Other code would go here')
    print(func())
    
hai()
other(hai)

#Creating a Decorator
def new_decorator(func):
    
    def wrap_func():
        print("some extra code before executing the func")
        
        func()
        
        print("some extra code after executing te func ")
      
    return wrap_func  

def func_need_decorator():
    print("the function need decorator")
    
    
func_need_decorator()
## Reassign func_needs_decorator
func_need_decorator=new_decorator(func_need_decorator)
func_need_decorator()

#A decorator simply wrapped the function and modified its behavior. Now let's understand how we can rewrite this code using the @ symbol, which is what Python uses for Decorators:

@new_decorator
def func_need_decorator():
    print("This function is in need of a Decorator")

func_need_decorator()
    