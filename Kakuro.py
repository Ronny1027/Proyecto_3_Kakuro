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
#Función para hacer la cuadricula
def dibujar_cuadricula(canvas):
    for i in range(FILAS + 1):
        canvas.create_line(0, i * TAM_CELDA, COLUMNAS * TAM_CELDA, i * TAM_CELDA)
    for j in range(COLUMNAS + 1):
        canvas.create_line(j * TAM_CELDA, 0, j * TAM_CELDA, FILAS * TAM_CELDA)
def juego():
    jueg = tk.Toplevel(kaku)
    jueg.title("Jugar Kakuro")
    jueg.geometry("700x600")
    #Frame general para acomodar los frames.
    frame_principal = tk.Frame(jueg)
    frame_principal.pack(padx=10, pady=10)

    #Frame para agrupar los elementos de la izquierda.
    frame_tablero = tk.Frame(frame_principal)
    frame_tablero.grid(row=0, column=0, padx=5)

    ancho_canvas = COLUMNAS * TAM_CELDA + 1
    alto_canvas = FILAS * TAM_CELDA + 1
    canvas = tk.Canvas(frame_tablero, width=ancho_canvas, height=alto_canvas, bg="white", highlightthickness=0)
    canvas.grid(row=0, column=0)
    dibujar_cuadricula(canvas)

    btn_ini = tk.Button(frame_tablero, text="Iniciar juego", bg="hotpink")
    btn_ini.grid(row=1, column=0, pady=5)

    #Frame para agrupar las opciones de la derecha(nombre,numeros y botones)
    frame_opciones = tk.Frame(frame_principal)
    frame_opciones.grid(row=0, column=1, padx=20, sticky="n")
    #Subframe del frame_opciones para acomodar todo mejor.
    frame_contenido = tk.Frame(frame_opciones)
    frame_contenido.pack(pady=10, fill="x")

    # Etiqueta de jugador
    tk.Label(frame_contenido, text="Jugador:").pack()
    tk.Entry(frame_contenido, width=25).pack(pady=5)

    # Números del 1 al 9
    btn1 = tk.Button(frame_contenido, text="1", width=6, height=1, bg = "green")
    btn1.pack(pady=7)
    btn2 = tk.Button(frame_contenido, text="2", width=6, height=1, bg = "green")
    btn2.pack(pady=7)
    btn3 = tk.Button(frame_contenido, text="3", width=6, height=1, bg = "green")
    btn3.pack(pady=7)
    btn4 =tk.Button(frame_contenido, text="4", width=6, height=1, bg = "green")
    btn4.pack(pady=7)
    btn5 = tk.Button(frame_contenido, text="5", width=6, height=1, bg = "green")
    btn5.pack(pady=7)
    btn6 =tk.Button(frame_contenido, text="6", width=6, height=1, bg = "green")
    btn6.pack(pady=7)
    btn7 = tk.Button(frame_contenido, text="7", width=6, height=1, bg = "green")
    btn7.pack(pady=7)
    btn8 =tk.Button(frame_contenido, text="8", width=6, height=1, bg = "green")
    btn8.pack(pady=7)
    btn9 =tk.Button(frame_contenido, text="9", width=6, height=1, bg = "green")
    btn9.pack(pady=7)
    #Boton especial de borrar
    tk.Button(frame_contenido, text="Borrar",width=8,).pack(pady=5)
    
    #Para agrupar los botones con opciones especiales(iniciar,guardar,etc)
    frame_botones = tk.Frame(frame_opciones)
    frame_botones.pack(pady=10, fill="x")

    btn_desh = tk.Button(frame_botones, text="Deshacer jugada",width=12, bg="lightgreen")
    btn_desh.grid(row=0, column=0, pady=5,padx=5)

    btn_reh = tk.Button(frame_botones, text="Rehacer jugada",width=12, bg="lightblue")
    btn_reh.grid(row=1, column=0, pady=5,padx=5)

    btn_borrar = tk.Button(frame_botones, text="Borrar juego",width=12, bg="cyan")
    btn_borrar.grid(row=0, column=1, pady=5,padx=5)

    btn_term = tk.Button(frame_botones, text="Terminar juego",width=12, bg="blue")
    btn_term.grid(row=1, column=1, pady=5,padx=5)

    btn_guardar = tk.Button(frame_botones, text="Guardar juego",width=12, bg="orange")
    btn_guardar.grid(row=0, column=2, pady=5,padx=5)

    btn_cargar = tk.Button(frame_botones, text="Cargar juego",width=12, bg="sienna")
    btn_cargar.grid(row=1, column=2, pady=5,padx=5)

    btn_record = tk.Button(frame_botones, text="Records",width=12, bg="yellow")
    btn_record.grid(row=1, column=3, pady=5,padx=5)
    
    
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
