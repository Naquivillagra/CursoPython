import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

#variosProductos=[
	
	#("Camiseta", 10, "Deportes"),
	#("Jarrón", 90, "Cerámica"),
	#("Camión", 20, "Juguetería")


#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

#print(variosProductos)

for producto in variosProductos:

	print("Nombre Artículo: ", producto[0], " Sección ", producto[2])

miConexion.commit()




miConexion.close()