def devuelve_ciudades(*ciudades): #el * significa que va a recibir un número indeterminado de elementos
	for elemento in ciudades:
		#for subELemento in elemento: #es un bucle for anidado
		yield from elemento #ahora estamos alamcenando los subelemntos, que serían las letras de las ciudades


ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))