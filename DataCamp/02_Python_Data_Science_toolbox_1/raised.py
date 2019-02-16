#!/usr/bin/env python3


def raise_val(n):

    x = 10

    def inner():
        nonlocal x
        raised = x ** n
        return raised

    return inner()


quadrado = raise_val(2)
print(quadrado)

cubo = raise_val(3)
print(cubo)