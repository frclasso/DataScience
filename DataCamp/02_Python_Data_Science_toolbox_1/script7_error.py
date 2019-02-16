#!/usr/bin/env python3

def sqrt(x):

    try:
        if x < 0:
            raise ValueError('x nao pode ser negativo')
        else:
            return x ** 0.5
    except TypeError:
        print('x precisa ser int ou float')


print(sqrt())