import math

print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número por favor: "))

intentos=0

while numero<0:
	print("No se puede hallar la raíz de un número negativo")

	if intentos==2: #esta línea recién se va a ejecutar en el tercer intento, cuando la variable "intentos" haya valido 0,1 y 2
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break; #el break te saca del bucle del while

	numero=int(input("Introduce un número por favor: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))