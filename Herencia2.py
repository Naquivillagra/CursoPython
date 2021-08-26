class Vehículos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
#cosas que va a poder hacer el vehículo: arrancar, acelerar, frenar, informarnos de su estado
	def arrancar(self):

		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)



class Furgoneta(Vehículos):

	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"

class Moto(Vehículos): #realmente la clase moto tiene 6 métodos. 5 que está heredando (el constructor y los 4 de abajo) que tiene la clase vehículo más el suyo propio que definimos abajo
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)


class VEléctricos(Vehículos):
	def __init__(self, marca, modelo):

		super().__init__(marca, modelo)

		self.autonomia=100

	def cargarEnergia(self):

		self.cargando=True

miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado() #en este caso, el estado llama al estado de la clase "moto", porque pisó al primer estado

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

class BicicletaElectrica(VEléctricos,Vehículos): #hereda los métodos y las propiedades de las dos clases
#Cuando hay herencia múltiple, se le da prioridad al primer argumento
	pass

miBici=BicicletaElectrica("Orbea", "hj")

