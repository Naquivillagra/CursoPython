class Coche():
	largoChasis=250  #éstas son las 4 propiedades de la clase
	anchoChasis=120  #
	ruedas=4         #
	enmarcha=False   # significa que el vehículo se encuentra detenido
#lo siguiente es el método: tiene dos comportamientos (arrancar y estado)
	def arrancar(self): #self hace referencia al objeto perteneciente a la clase
		self.enmarcha=True

	def estado(self):
		if(self.enmarcha):
			return "El coche está en marcha"

		else:

			return "El choche está parado"


miCoche=Coche()  #instanciar una clase

print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, "ruedas")
miCoche.arrancar()  #llama al método "arrancar"

print(miCoche.estado())  #si no accediéramos al método "arrancar", el estado del coche sería "parado"

print("---------A continuación creamos el segundo objeto------------")

miCoche2=Coche()
print("El largo del coche es: ",miCoche2.largoChasis)
print("El coche tiene ", miCoche2.ruedas, "ruedas")
print(miCoche2.estado())		