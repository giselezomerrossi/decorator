def decorator(function):
    def wrapper():
        print("I'm before execution")
        function()
        print("I'm after execution")

    return wrapper

def another_function():
    print("I'm an argument!")

decorated_function = decorator(another_function)
decorated_function()