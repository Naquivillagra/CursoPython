def generaPares(limite): #el límete es necesario para limitar la lista

	num=1

	while num<limite:

		yield num*2  #yield es un generador (devuelve el número por 2)

		num=num+1

devuelvePares=generaPares(10)	


print(next(devuelvePares)) #devuelve el primer objeto

print("Aquí podría ir más código...")

print(next(devuelvePares)) #devuelve el segundo objeto porque ya lo llamé una vez antes

print("Aquí podría ir más código...")

print(next(devuelvePares))