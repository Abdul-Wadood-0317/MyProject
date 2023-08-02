# import module1 as m
# print(m.sum(5, 5))

# print(m.mul(5, 4))
from module1 import sum
print(sum(10,20))

from module1 import * # *means call all modules
print(sum(10,20))
print(mul(10, 20))



