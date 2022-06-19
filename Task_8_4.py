def val_checker(f_lambda):
    def _val_checker(f):
        def logger(num):
            if f_lambda(num):
                print(f(num))
            else:
                raise ValueError(f'wrong val {num}')

        return logger

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
a = calc_cube(-5)