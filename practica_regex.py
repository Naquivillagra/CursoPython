import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

'''#print(re.search("aprender", cadena)) #el primer parámetro es la palabra que queremos buscar y el segundo parámetro es el lugar

textoBuscar="aprender"

textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start()) #caracter en el que empieza la palabra buscada

print(textoEncontrado.end()) #caracter en el que termina la palabra

print(textoEncontrado.span()) #devuelve en una tupla los dos caracteres anteriores'''

textoBuscar="Python"

print(len(re.findall(textoBuscar, cadena)))