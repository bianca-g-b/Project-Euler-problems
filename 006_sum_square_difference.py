# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385,

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from math import pow
sum_of_squares=0
squares_of_sum=0
for i in range(1,101):
    sum_of_squares+=pow(i,2)
    squares_of_sum+=i
    
squares_of_sum=pow(squares_of_sum,2)

diff=int(squares_of_sum-sum_of_squares)
print(diff)
    

