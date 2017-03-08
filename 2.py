# Programa que cuenta todos las imagenes

import json

with open("imagenes.json") as data_file:
	data = json.load(data_file)

contador = 0

for a in data["results"]["bindings"]:
	contador = contador + 1	

print " "
print "El numero total de imagenes es: " + str(contador)
print " "
