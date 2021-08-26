edad=input("Introduce la edad: ")


while(edad.isdigit()==False): #isdigit para que compruebe que el valor introducido es numérico

	print("Por favor, introduce un valor numérico")

	edad=input("Introduce la edad: ")

if (int(edad)<18):

	print("No puede pasar")
else:
	print("Puedes pasar")