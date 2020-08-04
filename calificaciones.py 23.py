# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:10:59 2020

@author:Carolina Chacha Jimenez
"""
# s=Primera calificacion
# b=Segunda calificacion
# e=Tercera calificacion
# Y=la suma de las dos mejores calificaciones

s=int(input("ingrese su primera calificacion :"))

b=int(input("ingrese su segunda calificacion :"))

e=int(input("ingrese su tercera calificacion :"))

if s>=e and b>=e :
    Y=s+b
else:
    if s>=b and e>=b:
        Y=s+e
    else :
        Y=b+e
print("su calificacion total es :",Y)