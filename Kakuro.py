#Modulos o importaciones necesarias para el programa.
import tkinter as tk


#Para emitir errores.
from tkinter import messagebox

#Para manipular archivos de información.
import json
#Función de juego
#Variables para poder hacer la cuadricula
FILAS = 9
COLUMNAS = 9
TAM_CELDA = 50
def dibujar_cuadricula(canvas):
    for i in range(FILAS + 1):
        canvas.create_line(0, i * TAM_CELDA, COLUMNAS * TAM_CELDA, i * TAM_CELDA)
    for j in range(COLUMNAS + 1):
        canvas.create_line(j * TAM_CELDA, 0, j * TAM_CELDA, FILAS * TAM_CELDA)
def juego():
    jueg = tk.Toplevel(kaku)
    jueg.title("Jugar Kakuro")
    jueg.geometry("700x600")
    ancho_canvas = COLUMNAS * TAM_CELDA + 1
    alto_canvas = FILAS * TAM_CELDA + 1

    canvas = tk.Canvas(jueg, width=ancho_canvas, height=alto_canvas, bg="white", highlightthickness=0)
    canvas.grid(row=0, column=0, padx=10, pady=10)

    dibujar_cuadricula(canvas)
    

    dibujar_cuadricula(canvas)
    

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
menubar.add_command(label = "Cerrar", command= kaku.destroy)


kaku.mainloop()
