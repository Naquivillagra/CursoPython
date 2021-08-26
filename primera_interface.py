from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas") #le da el título a la ventana

#raiz.resizable(1,0) #permite redimensionar a lo ancho pero no a lo alto

#raiz.geometry("650x350") #650 de ancho y 350 de alto

raiz.config(bg="blue") #color del cuadro

raiz.config(bd=35)

raiz.config(relief="sunken") #cambiamos el tipo de borde

raiz.config(cursor="pirate")

miFrame=Frame()

#miFrame.pack(side="left", anchor="n") #el Frame aparece anclado en donde le indique (n significa "norte")
#miFrame.pack(fill="x") #el Frame se expande horizontalmente
#miFrame.pack(fill="both", expand="True") 
miFrame.pack()

miFrame.config(bg="red") #el Frame es rojo pero la raíz sigue siendo azul

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="groove") #cambiamos el tipo de borde

miFrame.config(cursor="hand2") #el cursor se transforma en una mano dentro del Frame

raiz.mainloop() #mainloop siempre debe estar al final