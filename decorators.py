import functools
# Define your decorators here.
# Decorators wrap a function and performs some modifications before executing
# the function it is decorating.

def world(func):
    # This first line fixes help(func), __name__ , __doc__ ,
    # and other issues with introspection. Use it whenever you write
    # any new decorator.
    @functools.wraps(func)
    def wrapper():
        print(70*"=")
        func()
        print("World\n")
    return wrapper


def kanye(func):
    @functools.wraps(func)
    def wrapper():
        print(70*"=")
        print("\nI'm gonna let you finish, but")
        print("Beyonce had the best music video of all time.\n")
        func()
        print("\n")
    return wrapper


def twice_with_args(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        print(70*"=")
        print("\n")
        func(*args, **kwargs)
        func(*args, **kwargs)
        print("\n")
    return wrapper_do_twice


def fun_with_return(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(70*"=")
        print("\n")
        return func(*args, **kwargs)
        print("\n")
    return wrapper

# Follow this boiler plate for more
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
