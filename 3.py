# -*- coding: utf-8 -*-

# Introducir un siglo por teclado y busca en el fichero cuantas imagenes tienen están talladas en ese siglo

import json
import math

siglo = raw_input("Introduce el siglo: ")

Unidad = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

def convertir(numero):
	if numero.startswith("X"):	
		return numero
	else:
		N = numero[0:2:]
		N = int(N) + 1
		u = int(N) % 10
		d = int(math.floor(int(N)/10)) % 10
		c = int(math.floor(int(N)/100))
		if (N >= 100): 
			return(Centena[c]+Decena[d]+Unidad[u])
		else:
			if (N >= 10):
				return(Decena[d]+Unidad[u])
			else:
				return(Unidad[N])

with open("imagenes.json") as data_file:
	data = json.load(data_file)

for a in data["results"]["bindings"]:
	numero = a["om_talladoEn"]["value"]
	if convertir(numero) == siglo:
		print a["rdfs_label"]["value"]
