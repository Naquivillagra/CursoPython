mitupla=("Juan", 13, 1, 1995)
milista=list(mitupla) # esta variable almacena el valor de la tupla como lista
##print(mitupla[1]) #me imprime el elemento de la posición 1 de la tupla
print(mitupla)

milista1=["Juan", 13, 1, 1995]
mitupla1=tuple(milista) # transforma una lista en tupla
print(mitupla1)
print("Juan" in mitupla1)

print(mitupla1.count(13)) #cuenta las veces que aparece ese elemento en la tupla
print(len(mitupla1)) #cuenta la longitud de la tupla, cuántos elementos tiene

nombre, día, mes, año=mitupla #asignamos los nombres a cada elemento de la tupla
print(nombre)
print(día)
print(año)
print(mes)
