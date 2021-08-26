class Areas:

	"""Esta clase calcula las áreas de diferentes figuras geométricas"""

	def areaCuadrado (lado):

		"""Calcula el área de un cuadrado
		elevando al cuadrado el lado pasado por parámetro"""

		return "El área del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base, altura):

		"""Calcula el área de un triángulo utilizando los parámetros base y altura"""

		return "El área del triángulo es: " + str((base*altura)/2)



help(Areas)