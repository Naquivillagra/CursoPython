from io import open

#archivo_texto=open("archivo.txt","w") #crea un archivo externo de texto. La "w" significa archivo de escritura (write)

#frase="Estupendo día para estudiar Python \n el miércoles"

#archivo_texto.write(frase)

#archivo_texto.close()

#archivo_texto=open("archivo.txt","r") #"r" es de read

#texto=archivo_texto.read()

#archivo_texto.close()

#print(texto)

#lineas_texto=archivo_texto.readlines() #convierte el archivo en una lista

#archivo_texto.close()

#print(lineas_texto[0]) #permite acceder a los distintos elementos de la lista

archivo_texto=open("archivo.txt","a") #"a" de append. Es para agregar algo

archivo_texto.write("\n siempre es una buena ocasión para estudiar Python")

archivo_texto.close()