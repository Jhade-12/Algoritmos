# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:17:03 2020

@author: Carolina Chacha
"""


def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)
for x in range(8):
    print(fib(x))
    