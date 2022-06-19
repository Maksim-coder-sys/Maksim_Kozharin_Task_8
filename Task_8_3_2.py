import re

def type_logger(f):
    def logger(num):
        rez = f(num)
        name_func = (re.findall(r'\s(.+)\s[a]',str(f)))[0]
        return f'{name_func}({num}: {type(num)})\n{num} в степени 3 = {rez}'
    return logger
@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
print(a)