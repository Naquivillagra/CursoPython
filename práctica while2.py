edad=int(input("Introduce tu edad por favor: "))

while edad<5 or edad>100:
	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
	edad=int(input("Introduce tu edad por favor: ")) #el bucle se va a ejecutar infinamente hasta que la edad sea correcta

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))