#!/usr/bin/env python3

# map recebe uma função e uma sequencia


# nums = [48, 6,9, 21, 1]
#
# square_all = map(lambda num:num**2, nums)
#
# print(square_all)
# print(list(square_all))


num1 = [4,5,6]
num2 = [5,6,7]
result = map(lambda n1,n2:n1+n2, num1,num2)
print(list(result))