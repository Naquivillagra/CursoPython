nombre="Píldoras informáticas"

contador=0

for i in nombre:

	if i==" ":
		continue #el bucle ignora las instrucciones cuando se encuentra un espacio en blanco
	contador+=1 #es lo mismo que poner contador=contador+1


print(contador)