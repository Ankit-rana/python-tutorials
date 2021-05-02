# function taking other function as arg and modifying its behavior
# eg. @route(url) above foo(env) or (route(url))(foo(env))

def route(url):                                  # decorator argument
    def inner(foo):                            # function modified
        print("general extended logic")
        def wrapper(*args, **kwargs):              # argument to function modified. 
            return foo(*args, **kwargs)          
        return wrapper
    return inner

@route("/")
def view(environ):
    print("buisness logic in %s " % environ)


view("linux64")

# 2. above syntax creates problem while debugging like

print(view.__name__) # wrapper

# To solve that, always use functools.wraps decorator
from functools import  wraps

def route(url):                                  
    def inner(foo):                            
        print("general extended logic")
        @wraps(foo)
        def wrapper(*args, **kwargs):             
            return foo(*args, **kwargs)          
        return wrapper
    return inner

@route("/")
def view(environ):
    print("buisness logic in %s " % environ)

view("linux64")
print(view.__name__) # view