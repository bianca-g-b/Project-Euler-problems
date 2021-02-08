# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import numpy as np
m=999
n=100
def pal(n,m):
    p=[]
    

    for i in range(m,n-1,-1):
        for j in range(m,n-1,-1):
            x=str(i*j)
            if x==x[::-1]:
                p+=[int(x)]
    d=np.array(p)
    return np.max(d)
        
            
print(pal(n,m))
        
