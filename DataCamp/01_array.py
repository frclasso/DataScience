#!/usr/bin/ev python3

height = [1.73, 1.68,  1.84, 1.89, 1.79]

weight = [65.9, 70.3, 80.4, 56.6, 70.2]

# print(width / height ** 2)
# Error
# TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'



import numpy as np

np_height = np.array(height)

np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
#print(bmi)  #  [22.01877777 24.90787982 23.74763705 15.84502114 21.90942854]

#print(bmi[1])
print(bmi < 16) #[False False False  True False]