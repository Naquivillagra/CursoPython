from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="Homero.gif")

#miLabel=Label(miFrame, text="Hola alumnos de Python")
#miLabel.place(x=100, y=200) #permite ubicar el texto en cualquier lugar de nuestra coordenada gráfica
#Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200) #una forma de abreviar lo anterior
Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()