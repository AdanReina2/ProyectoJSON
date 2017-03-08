# -*- coding: utf-8 -*-

# Introducir por teclado un nombre de imagen y mostrar por pantalla la url y el año de talla de la misma.

import json

imagen = raw_input("Introduce la imagen a buscar: ")

with open("imagenes.json") as data_file:
	data = json.load(data_file)

for a in data["results"]["bindings"]:
	if a["rdfs_label"]["value"] == imagen:
		print "La URL es: " +str(a["uri"]["value"])
		print "Año de talla: " +str(a["om_talladoEn"]["value"])

