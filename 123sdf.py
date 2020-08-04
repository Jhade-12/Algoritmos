# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:42:36 2020

@author: pc
"""

def es_bisiesto(año):
    if año %400==0:
        return True
    elif año %100==0:
        return False
    elif año %4==0:
        return True
    else:
        return False

testData=[1930, 2020, 2006,1907]

testResuilts=[0,0,0,0]
for i in range(len(testData)):
    testResuilts[i]=es_bisiesto(testData[i])
print(testResuilts)
