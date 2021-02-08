# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def prime(num):
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True
    

def the_10001st(n):
    x=0
    d=3
    while x < (n-2):
        d+=2
        if prime(d):
            x+=1
        else:
            pass
    return d
        
    
print(the_10001st(10001))

    
    

        
        

