#!/usr/bin/env python3

def print_all(**kwargs):

    for k, v in kwargs.items():
        print(k + ':' + v)


print_all(name='Fabio',education='Graduation Degree', job='Programmer', enterprise='CodeCla' )