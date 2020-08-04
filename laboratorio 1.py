# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:52:33 2020

@author: pc Carolina Chacha Jimenez
""" 


def isYearLeap(año):
#
    if año %400==0:
        return True
    elif año %100==0:
        return False
    elif año %4==0:
        return True
    else:
        return False


#

def daysInMonth(year, month):
    
#
    if  isYearLeap(year) == False:
        diasMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        diasMes = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days=0;
    for i in range(month):
        days=diasMes[i]
    return days
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
#    if (mo >13):        print('None')
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
    
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
