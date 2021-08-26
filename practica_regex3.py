import re

lista_nombres=['Ma.1',
				'Se1',
				'Ma2',
				'Ba1',
				'Ma:3',
				'Va1',
				'Va2',
				'Ma4',
				'MaA',
				'Ma.5',
				'MaB',
				'Ma:C']


for elemento in lista_nombres:
	if re.findall('Ma[.:]', elemento):

		print(elemento)