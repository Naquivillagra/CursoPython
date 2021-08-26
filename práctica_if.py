print("Programa de evalaución de notas de alumnos")

nota_alumno=input()

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion


print(evaluacion(int(nota_alumno)))