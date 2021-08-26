import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

#UPDATE actualiza el precio de la pelota en la base de datos

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")



miConexion.commit()

miConexion.close()