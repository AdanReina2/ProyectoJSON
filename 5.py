# -*- coding: utf-8 -*-

# Mostrar en pantalla la imagen mas recientemente tallada y la que mas años lleve tallada.

import json

with open("imagenes.json") as data_file:
	data = json.load(data_file)

mayor = 0
menor = 10000
tallamenor = 0
tallamayor = 0

for a in data["results"]["bindings"]:
	numero = a["om_talladoEn"]["value"]
	if not numero.startswith("X"):
		if int(numero) < menor:
			menor = int(numero)
			tallamenor = str(a["rdfs_label"]["value"])
		elif int(numero) > mayor:
			mayor = int(numero)
			tallamayor = str(a["rdfs_label"]["value"])
			
print "La imagen que lleva menos años tallada es: " + tallamayor
print "La imagen que lleva mas años tallada es: " + tallamenor


	
