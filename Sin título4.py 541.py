# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:06:25 2020

@author: pc Carolina Chacha
"""


nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=input("Ingrese su edad:")
edad=int(edad)
if edad >=1 and edad<=11:
    print("Usted es un niño/a")
elif edad >=12 and edad <=17:
    print("Usted es un adolescente")
elif edad >=18 and edad <=40:
    print("Usted es joven")
elif edad >=41 and edad <=62:
    print("Usted es un adulto")
elif edad >=63 and edad <=80:
    print("Usted es un adulto mayor")
else:
    print ("Usted es un adulto")
ubicación=input("Ingrese su ubicación:")

space= print("Su nombre es"+nombre,apellido+"usted tiene"+edad+"años"+"y vive en la ciudadela"+ubicación)