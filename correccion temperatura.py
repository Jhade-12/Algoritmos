# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:04:10 2020

@author: Carolina Chacha Jimenez
"""

print("Programa: Temperatura del agua")
temperatura = []
n = int(input("Numero ingresado de temperaturas del (1,10): "))
for i in range(n):
 num = int(input("Temperatura  °C :"))
 temperatura.append(num)
CGas = 0
CLiquido = 0
CSolido = 0
for num in temperatura:
    if (num==100 or num>100):
        CGas= CGas+1
    elif (num < 0 or num==0):
        CSolido=CSolido+1
    elif (num>0 or num<100):
        CLiquido= CLiquido+1
print()
print("!El analisis de muestras de aguas seran!")
print("Cantidad de muestras solidas:", CSolido)
print("Cantidad de muestras liquidas:", CLiquido)
print(":Cantidad de muestras gaseosas", CGas)
i=0
print("Introdusza de nuevo el valor de las temperaturas")
Tem1=int(input("Temperatura 1 en °C:"))
Tem2=int(input("Temperatura 2 en °C:"))
Tem3=int(input("Temperatura 3 en °C:"))
temT =(Tem1+Tem2+Tem3)
promC =temT/3
Fht1 =(Tem1 * 9/5)+32
Fht2 =(Tem2 * 9/5)+32
Fht3 =(Tem3 * 9/5)+32
promFht = (Fht1 + Fht2 + Fht3) / 3
print("Temperatura promedio en grados celsius °C:", promC)
print("Temperatuda promedio en grados  fahrenheit °F:", promFht)