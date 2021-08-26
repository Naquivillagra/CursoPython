contador=0
miEmail=input("Introduce tu dirección de email: ")

for i in miEmail: 

	if (i=="@" or i=="."): 

		contador=contador+1  #la variable "contador" va a valer 1 cuando el i valga @ y va a valer 2 cuando encuentr el "."

if contador==2:
	print("Email es correcto")
else:
	print("El email no es correcto")