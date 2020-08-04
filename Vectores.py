# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:35:05 2020

@author: Carolina Chacha Jimenez  G:2
"""


from random import randint
from time import sleep
preguntar=True
temp = int()
nombre=str()
lista=[int()for ind0 in range(100)]
while preguntar:
    print(" Terminar la ejecucion digite 0 caso contrario puede")
    print("Ingresar el tamaño del vector, recuerde que deber ser > que 3 y",
          "< que 30: ")  
    tamaño=int(input())
    if tamaño>=3 and tamaño<=30:
        while preguntar:  
            print("Intoduzca el tamaño del vector digite 0 caso elija las otras opciones")
            print("Para trabajar con números o con caracteres  digite 1 pero si es con números digite 2: ")
            pregu=int(input())
            if pregu==1 :
                for i in range(1,tamaño+1):
                    print("\nIngrese el nombre del estudiante",i) 
                    nombre=input()
                    lista[i-1]=nombre
                    print("El valor en la posicion ",i," es  ", lista[i-1])
                for j in range(1,tamaño+1):
                    for l in range(1,tamaño):
                        if lista[l-1]>lista[l]:
                            temp = lista[l-1]
                            lista[l-1]=lista[l]
                            lista[l]=temp
                for k in range(1,tamaño+1):
                    print("\n"*0)
                    print("El vector ordenado en la posicion ",k," es ",lista[k-1])
            elif pregu==0:
                break
            else:
                for i in range(1,tamaño+1):
                    lista[i-1]=randint(0,99)
                    print("\n"*0)
                    print("El valor en la posicion ",i," es  ", lista[i-1]) 
                    sleep(1)
                sleep(1)
                while preguntar:
                    print("Quiere regresar a trabajar con números o caracteres digite 0 caso contrario continue")
                          
                    print(" Para ordenar de a > digite 1 o quiere de > a < digite 2: ")
                    pre=int(input())
                    if pre == 1:
                        for j in range(1,tamaño+1):
                            for l in range(1,tamaño):
                                if lista[l-1]>lista[l]:
                                    temp = lista[l-1]
                                    lista[l-1]=lista[l]
                                    lista[l]=temp
                        for k in range(1,tamaño+1):
                            print("\n"*0)
                            print("El vector ordenado en la posicion ",k," es ",lista[k-1])
                    elif pre==0:
                        break
                    else:
                        for j in range(1,tamaño+1):
                            for l in range(1,tamaño):
                                if lista[l-1]<lista[l]:
                                    temp = lista[l-1]
                                    lista[l-1]=lista[l]
                                    lista[l]=temp
                        for k in range(1,tamaño+1):
                            print("\n"*0)
                            print("El vector ordenado en la posicion ",k," es ",lista[k-1])
                            
    elif tamaño>30:
        print("El numero que usted a ingresado es < a 30,",
              "porfavor vuelva a ingresar otro número")
    elif tamaño== 0:
        preguntar = False
    
    else:
        print("El numero que usted a ingresado es > a 3,",
              "porfavor vuelva a ingresar otro número")