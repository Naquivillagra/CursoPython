def divide():

	try:

		op1=(float(input("Introduce el primer número: ")))

		op2=(float(input("Introduce el segundo número: ")))

		print("La división es: " + str(op1/op2))

	#except ValueError: #se puede poner solo "except" para hacer una excepción general, sin especificar el tipo de error

		#print("El valor introducido es erróneo")

	#except ZeroDivisionError:

		#print("No se puede dividir entre 0!")

	finally: # con el finally puede dar error, pero el programa se sigue ejecutando

		print("Cálculo finalizado")

divide()