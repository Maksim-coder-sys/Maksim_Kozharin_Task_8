from functools import wraps
def type_logger(func):
    def inner(*args, **kwargs):
        print((type)(func(*args, **kwargs)))
    return inner

@type_logger
def calc_cube(x):
    return x ** 3

@type_logger
def new_string(x):
    return x

@type_logger
def mult_num(x, y):
    return x * y




mult_num(4, 5.8)

new_string('City')

calc_cube(5)



