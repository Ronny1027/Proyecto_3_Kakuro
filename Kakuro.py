#Modulos o importaciones necesarias para el programa.
import tkinter as tk

#Para ventanas emergentes.
from tkinter import *

#Para emitir errores.
from tkinter import messagebox

#Para manipular archivos de información.
import json
#Función de juego
def juego():
    jueg = tk.Toplevel(kaku)
    jueg.title("Jugar Kakuro")
    jueg.geometry("700x600")

#Interfaz grafica principal.
kaku = tk.Tk()

kaku.title("Menú principal - Kakuro")#Titulo de la ventana

kaku.geometry("600x400")#Vista de la ventana, ancho x alto


menubar = tk.Menu(kaku)
kaku.config(menu=menubar)


filemenu = tk.Menu(menubar, tearoff=0)

menubar.add_command(label="Jugar",command=juego)


menubar.add_command(label="Configuración")
menubar.add_command(label = "Acerca de")


menubar.add_command(label = "Ayuda")
menubar.add_command(label = "HOLA", command= kaku.destroy)


kaku.mainloop()
