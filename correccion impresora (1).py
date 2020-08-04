# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:04:10 2020

@author: Carolina Chacha Jimenez
"""


if __name__ == '__main__':
	contadorinicial = int()
	contadorfinal = int()
	op = int()
	contadortotal = int()
	costobn = float()
	costocolor = float()
	costobn = 0.06
	costocolor = 0.12
	contadortotal = 0
	while True:# no hay 'repetir' en python
		print("Valor inicial")
		contadorinicial = int(input())
		if contadorinicial>0: break
	while True:# no hay 'repetir' en python
		print("Valor final")
		contadorfinal = int(input())
		if (contadorfinal<=contadorinicial):
			print("Error")
		if contadorfinal>=contadorinicial: break
	while True:# no hay 'repetir' en python
		print("Impresora (1. B/N, 2.- Color): ")
		op = int(input())
		if (op>1 or op<2) and op>0: break
	contadortotal = contadorfinal-contadorinicial
	print("Impresiones = ",contadortotal)
	if (op==1):
		print("Costo= $ ",contadortotal*costobn)
	else:
		print("Costo= $ ",contadortotal*costocolor)
