class Coche():

	def __init__(self): #esto es el constructor de la clase. Es lo que le va a dar el estado inicial a los objetos de esta clase
		
		self.__largoChasis=250  
		self.__anchoChasis=120  
		self.__ruedas=4       #estamos encapsulando el valor de esta propiedad (no se podrá modificar desde el exterior de esta clase)  
		self.__enmarcha=False   

	def arrancar(self,arrancamos): #le agregamos un parámetro al método
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			return "El coche está en marcha"

		else:

			return "El choche está parado"


	def estado(self):
		print("El coche tiene " , self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
		



miCoche=Coche()  

print(miCoche.arrancar(True))  

miCoche.estado()  

print("---------A continuación creamos el segundo objeto------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.__ruedas=2 #aunque se intente modificar el valor de las ruedas, no se puede porque está encapuslada

miCoche2.estado()		