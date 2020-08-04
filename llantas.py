# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:30:18 2020

@author: Carolina Chacha Jimenez
"""


#Compra de las llantas 

#llantas=Cantidad de llantas
#unitario=Presio unitario 
#pagar=  Valor a pagar 

llantas=int(input("Catidad de llantas:")) 

unitario=float(input("Presio unitario:")) 

if llantas>4:
     unitario=0.9*unitario
     
pagar=unitario*llantas


print("Valor de pagar:",pagar)     