# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:00:02 2020

@author: Carolina Chacha Jimenez
"""


import numpy as np
from random import randint
print("\n Admitir las  filas  que se requieren: ")
filas=int(input())    
print("\n Andmitir cuantas columnas se requieren: ")
columnas=int(input())
print("\n"*0)
matriz=np.zeros([filas,columnas])
u=-1
c=-1
e=filas
g=filas
for i in range(0,filas):
    for n in range(0,columnas):
        matriz[i][n]=int(randint(0,99))
print("<< Matriz  de",filas,"x",columnas,">>")
print("\n"*0)
print(matriz)
print("\n"*0)
print('El valor requerido de la diagonal principal de la matriz es: ')
print("\n"*0)
for j in range(0,filas):
    if u<filas:
        u+=1
        e-=1
    print(' | -- |'*u,"|",int(matriz[j][u]),"|",'| 0 | '*e)
    
print('\n El valor de la diagonal secundaria de la matriz es: ')
print("\n"*0)
for k in range(0,filas):
    if c<filas:
        c+=1
        g-=1
    print(' | -- |'*g,"|",int(matriz[k][g]),"|",'| 0 | '*c)
