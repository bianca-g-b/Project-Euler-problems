# -*- coding: utf-8 -*-
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

#recursion method
def recur_mult(i):
    i-=1
    if i<=0:
        return i
    if i%3==0 or i%5==0:
        return i + recur_mult(i)
    else:
        return recur_mult(i)
    
print(recur_mult(1000))

#iteration method
def iter_mult(i):
    t=0
    for i in range(i):
        if i%3==0 or i%5==0:
            t+=i
    return t

print(iter_mult(1000))