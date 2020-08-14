def validate_user(user):
    def decorator(function_called):
        def inner(*args, **kwargs):
            if user == 'gisele':
                return function_called(*args, **kwargs)
            else:
                raise AttributeError
        return inner
    return decorator

@validate_user("gisele")
def my_function():
    print('you have permission!')

my_function()
