#!/usr/bin/env python
# -*- coding:utf-8 -*-  

from math import sqrt

def is_prime(x):
    if x==1:
        return False
    k= int(sqrt(x))
    for j in range(2,k+1):
        if x%j ==0:
            return False
        return True

for i in range(2,101):
    if is_prime(i):
        print i
    