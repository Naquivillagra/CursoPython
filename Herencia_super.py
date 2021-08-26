class Persona():

	def __init__(self, nombre, edad, Lugar_residencia):

		self.nombre=nombre

		self.edad=edad

		self.lugar_residencia=Lugar_residencia

	def descripcion(self):

		print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia)


class Empleado(Persona): #la clase empleado hereda las propiedades de la clase "Persona". Principio de sustitución: un empleado es siempre una persona pero no viceversa.

	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #el comando "super" está llamando al método "init" de la clase padre

		self.salario=salario

		self.antigüedad=antigüedad

	def descripcion(self):

		super().descripcion() #Ejecuta la descripción de la clase "persona"

		print(" Salario: ", self.salario, " Antigüedad: ", self.antigüedad)



Manuel=Persona("Manuel", 55, "Colombia")

Manuel.descripcion() #la descrípción está haciendo referencia a la del "Empleado"

print(isinstance(Manuel,Empleado)) #devuelve True porque "Manuel" es de la clase empleado
                                   #devuelve False porque no toda persona es empleado