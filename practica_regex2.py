import re

lista_nombres=['hombres',
			'mujeres',
			'mascotas',
			'camión',
			'camion'
				]


for elemento in lista_nombres:
	if re.findall('cami[oó]n', elemento):	#para buscar la palabra camion con y sin tilde

		print(elemento)