#!/usr/bin/python3

rango = range(11)

for primero in rango:
	print("Tabla del", primero)

	for segundo in rango:
		resultado = primero*segundo
		print(str(primero) + " por " + str(segundo)  + " es "+ str(resultado))
	
