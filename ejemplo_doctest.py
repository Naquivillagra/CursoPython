def compruebaMail(mailUsuario):

	"""
	la función compruebaMail evalúa un mail recibido
	en busca del @. Si tiene un @ es correcto, si tiene más de un 
	@ es incorrecto, si el @ está al final es incorrecto


	>>> compruebaMail('juan@cursos.es')
	True

	>>> compruebaMail('juancursos.es@')
	False

	>>> compruebaMail('juancursos.es')
	False

	>>> compruebaMail('juan@cursos@.es')
	False

	"""
	arroba=mailUsuario.count('@')

	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False

	else:
		return True

import doctest
doctest.testmod()