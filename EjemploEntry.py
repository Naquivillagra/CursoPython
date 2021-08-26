from tkinter import*

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre) #creo un cuadro de texto
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right") #para escribir en rojo en este cuadro de texto

cuadroPass=Entry(miFrame) 
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame) 
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame) 
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10) #padx y pady se usan para separar en determinados pixeles los cados de texto y los labels

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview) 
scrollVert.grid(row=4, column=2, sticky="nsew")  #creamos la barra de scroll. con "nsew" hacemos que se adapte al cuadro de comentarios

textoComentario.config(yscrollcommand=scrollVert.set) #es para que la barra de scroll se desplace correctamente

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) #siticky se usa para ubicar el label. "e" de east (este)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

def codigoBoton():

	minombre.set("Juan") #al pulsar "enviar" aparece el nombre

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton) #agrega un botón

botonEnvio.pack()


raiz.mainloop()