#!/usr/bin/env python
# -*- coding:utf-8 -*-  

from random import randint

x=randint(0,10)
flag = raw_input('进入请按A，退出请按Q')
if(flag=='A'):
    for iter_var in range(3):
        y = input('please enter a number')
        if x==y:
            print "Yes"
            break
        elif x<y:
            print "No smaller"
        else:
            print "No bigger" 
        print '退出请按Q,继续请按A'
        flag = raw_input()
        print flag
        
            
else:
    print 'GoodBey'