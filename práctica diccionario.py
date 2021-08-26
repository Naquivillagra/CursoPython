midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}
print(midiccionario["Francia"]) #me devuelve el valor asignado a Francia
midiccionario["Italia"]="Roma" # agrega una pareja más al diccionario
print(midiccionario) #imprime el diccionario completo
del midiccionario["Reino Unido"] #elimina un elemento del diccionario
print(midiccionario)
midiccionario1={"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}
print(midiccionario1)

mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario2={mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Londres", mitupla[3]:"Berlín"} #arma un diccionario a partir de una tupla, asignando una pareja a los elementos
print(midiccionario2)

midiccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}} #creo un diccionario dentro de otro diccionario
print(midiccionario3)
print(midiccionario3["anillos"])
print(midiccionario3.keys()) #imprime todas las claves que pertencen al diccionario
print(midiccionario3.values()) #imprime los valores del diccionario
print(len(midiccionario3)) #longitud del diccionario, tiene 4 parejas
