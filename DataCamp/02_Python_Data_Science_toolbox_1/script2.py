#!/usr/bin/env python3

num =5

def func1():
    num = 3
    print(num)

def func2():
    global num
    double_num = num * 2
    num =6
    print(double_num)


func1()
func2()
print(num)