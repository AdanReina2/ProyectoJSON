# Programa que lista todas las imagenes

import json

with open("imagenes.json") as data_file:
	data = json.load(data_file)

print " "
print "La lista de imagenes es la siguiente: "
print " " 

for a in data["results"]["bindings"]:
	print a["rdfs_label"]["value"]
	
print " "
