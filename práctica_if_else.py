print("Verificación de acceso")

edad_usuario=int(input("Introduce tu edad, por favor: ")) # el int es para transformar en número entero el input, que siempre viene como str

if edad_usuario<18:
	print("No puedes pasar")
elif edad_usuario>100:
	print("Edad incorrecta")
else:
	print("Puedes pasar")

print("El programa ha finalizado")