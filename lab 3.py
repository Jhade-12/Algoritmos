# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:37:04 2020

@author: Carolina Chacha
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

    # Caso de años diferentes



    
def diasHastaFecha(day1, month1, year1, day2, month2, year2):  # Días restante primer añ
    if es_bisiesto(year1) == False:
        diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    i = month1+1  ## +1  meses .
    restoYear =  diasMes[i-1] -day1
    
    while i < 12:
        restoYear = restoYear + diasMes[i] ##  que pasan con los  días intermedios 
        i = i + 1
    
    primerYear =  restoYear ## restomes
      
    
    if es_bisiesto(year2) == False:
        diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    llevaYear = 0
    lastYear = 0
    i = 0
    while i < month2:
        llevaYear = llevaYear + diasMes[i] # i=i+1  es lo mismo i+=1
        i = i + 1
    
    lastYear = day2 + llevaYear 
    
    return  primerYear+day2 + lastYear
def totaldias(day1, month1, year1, day2, month2, year2):
    total=0; 
    for i in range(year1+1,year2):
        if(es_bisiesto(i)==True):
            total+=366
        else:
            total+=365
    a=diasHastaFecha(day1, month1, year1, day2, month2, year2)
    total=total+a
    
    return total


def  contarias(day1, month1, year1, day2, month2, year2):
    if(month1>12 or month2>12):
        return None
    if(day1>31 or day2 > 31):
        return None
    if(year1>year2):
        return  totaldias(day1, month1, year1, day2, month2, year2)
    else:
        return totaldias(day2, month2, year2,day1, month1, year1)
    
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
c=0

while c<1:
   print(contarias(1,13,testYears[c],0,testMonths[c+1],testYears[c+1]))
   c+=1

   