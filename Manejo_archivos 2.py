from io import open

#archivo_texto=open("archivo.txt","r")

# archivo_texto.seek(11) #seek determina dónde va a ser el comienzo de la frase

#print(archivo_texto.read(11)) #lee hasta la posición 11

#print(archivo_texto.read())

#archivo_texto.seek(len(archivo_texto.read())/2)

#print(archivo_texto.read())

archivo_texto=open("archivo.txt","r+") #lectura y escritura

#archivo_texto.write("Comienzo del texto")

#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines();

lista_texto[1]=" Esta línea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()
