import datetime


def calculate_time_decorator(function):
    def calculate_time():
        print(datetime.datetime.now())
        function()
        print(datetime.datetime.now())

    return calculate_time

@calculate_time_decorator
def my_function():
    for i in range(10000000):
        continue

my_function()

