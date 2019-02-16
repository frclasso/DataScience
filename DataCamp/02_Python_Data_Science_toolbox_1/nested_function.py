#!/usr/bin/env python3


def mod2plus5(x1, x2,x3):

    def inner(x):
        return x % 2 + 5

    return inner(x1), inner(x2), inner(x3)


print(mod2plus5(1,2,3))