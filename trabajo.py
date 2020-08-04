# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:11:34 2020

@author: pc
"""


#v=Cantidad de horas trabajadas
#e=Tarifa por hora
#k=Descuento 
#u=Pago que recibe el obreo


v=int(input("Horas trabajadas: ")) 

e=int(input("Tarifa por horas:")) 

k=int(input("Descuentos:")) 

if v<=40:
    u=v*e-k
else: 
    
    u=40*e+1.5*e*(v-40)-k 
    
print("Valor a pagar:",u) 
