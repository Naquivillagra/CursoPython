class Coche():

	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")


class Moto():

	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")


class Camion():

	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")



def desplazamientoVehiculo(vehiculo): #polimorfismo. Se puede modificar el objeto abajo y cambia el vehículo al que hacemos referencia
	vehiculo.desplazamiento()


miVehiculo=Coche()

desplazamientoVehiculo(miVehiculo)