email=input("Introduce tu email, por favor: ")

for i in email:

	if i=="@":

		arroba=True

		break; #el programa se sale del bucle "for" y sigue con los códigos

else: #el else se va a ejecutar cuando el bucle ya esté vacío, pero forma parte del bucle "for"

	arroba=False

print(arroba)