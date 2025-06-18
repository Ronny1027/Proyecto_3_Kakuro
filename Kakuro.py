#Modulos o importaciones necesarias para el programa.
import tkinter as tk


#Para emitir errores.
from tkinter import messagebox

#Para manipular archivos de información.
import json
#Cargar las partidas de juego
def cargar_partida():
    with open("kakuro2025_partidas.json","r") as w:
        partidas = json.load(w)
        return partidas[0]
#Interfaz grafica de la configuración.
def configura():
    confi = tk.Toplevel(kaku)
    confi.title("Configuración de juego")
    confi.geometry("500x400")
    frame_nive = tk.Frame(confi)
    tk.Label(frame_nive, text="Configuración de juego", anchor='w').pack(padx=20)
    tk.Label(frame_nive, text="Nivel", anchor='w').pack(padx=20)
    frame_nive.pack(pady=10)
    difi_var = tk.StringVar(value="Fácil")  # valor por default
    tk.Radiobutton(frame_nive, text="Fácil", variable=difi_var, value="Fácil").pack(anchor="w", padx=20)
    tk.Radiobutton(frame_nive, text="Medio", variable=difi_var, value="Medio").pack(anchor="w", padx=20)
    tk.Radiobutton(frame_nive, text="Difícil", variable=difi_var, value="Difícil").pack(anchor="w", padx=20)
    tk.Radiobutton(frame_nive, text="Experto", variable=difi_var, value="Experto").pack(anchor="w", padx=20)
    
    frame_tiemp = tk.Frame(confi)
    frame_tiemp.pack(pady=10)
    tk.Label(frame_tiemp, text="Reloj", anchor='w').pack(padx=20)
    relo_var = tk.StringVar(value="crono")  # valor por default
    tk.Radiobutton(frame_tiemp, text="Cronómetro", variable=relo_var, value="crono").pack(anchor="w", padx=20)
    tk.Radiobutton(frame_tiemp, text="Temporizador", variable=relo_var, value="tempori").pack(anchor="w", padx=20)
    tk.Radiobutton(frame_tiemp, text="No usar reloj", variable=relo_var, value="sinrelo").pack(anchor="w", padx=20)
    #Entrys en caso de usar temporizador
    frame_tempo = tk.Frame(confi)
    frame_tempo.pack(pady=10)
    label_tempo = tk.Label(frame_tempo, text="Indique el tiempo(caso de temporizador)")
    label_tempo.grid(row =0,column=1)
    #Horas
    label_hora = tk.Label(frame_tempo, text="Horas")
    label_hora.grid(row =1,column=0)
    horas_entry= tk.Entry(frame_tempo,width=30)
    horas_entry.grid(row =1,column=1)
    #Minutos
    label_minu = tk.Label(frame_tempo, text="Minutos")
    label_minu.grid(row =2,column=0)
    minu_entry= tk.Entry(frame_tempo,width=30)
    minu_entry.grid(row =2,column=1)
    #Segundos
    label_segu = tk.Label(frame_tempo, text="Segundos")
    label_segu.grid(row =3,column=0)
    seguns_entry= tk.Entry(frame_tempo,width=30)
    seguns_entry.grid(row =3,column=1)
    #Función interna para guardar la informacion
    def guardar_info():
        #Se saca la información
        nivel = difi_var.get()
        reloj = relo_var.get()
        horas = horas_entry.get()
        minuts = minu_entry.get()
        segunds = seguns_entry.get()
        temporizador = "No hay"
        if reloj =="tempori":
            if horas or minuts or segunds:
            # Validar que todos sean números enteros.
                if (horas and not horas.isdigit()) or (minuts and not minuts.isdigit()) or (segunds and not segunds.isdigit()):
                    messagebox.showerror("Error", "Horas, minutos y segundos deben ser números enteros.")
                    return
                h = 0
                m = 0
                s = 0
                if horas != "":
                    h = int(horas)
                else:
                    h = 0
                if minuts!= "":
                    m = int(minuts)
                else:
                    m = 0
                if segunds!= "":
                    s = int(segunds)
                else:
                    s = 0
                if not (0 <= h <= 2):
                    messagebox.showerror("Error", "Horas debe estar entre 0 y 2.")
                    return
                if not (0 <= m <= 59):
                    messagebox.showerror("Error", "Minutos debe estar entre 0 y 59.")
                    return
                if not (0 <= s <= 59):
                    messagebox.showerror("Error", "Segundos debe estar entre 0 y 59.")
                    return
                # Se verifica que no se hayan escrito solo 0
                if h == 0 and m == 0 and s == 0:
                    messagebox.showerror("Error", "Debe ingresar al menos un valor diferente de cero para el temporizador.")
                    return
                # Si todos las validaciones se cumplen, se forma el temporizador completo.
                temporizador = f"{h:02}:{m:02}:{s:02}"#el 02 es para agregar ceros de relleno
            else:
                temporizador = "No hay"
        datos = {"Nivel":nivel,
                "Reloj":reloj,"Temporizador":temporizador}
        with open("kakuro2025_configuración", "w") as f:#Se abre la información.
            json.dump(datos, f, indent=4)#Se depositan los datos en archivo.json.
        confi.destroy
    frame_btons= tk.Frame(confi)
    frame_btons.pack(pady=10)
    btn_acept = tk.Button(frame_btons,text = "Aceptar",command=  guardar_info)
    btn_acept.grid(row=0, column=0,padx=5)
    btn_cancel = tk.Button(frame_btons,text = "Volver",command= confi.destroy)
    btn_cancel.grid(row=0, column=1,padx=5)
#Dibujar las especificaciones de la partida.
def dibujar_claves_y_casillas(canvas, claves):
    casillas = {}

    for clave in claves:
        f = clave["fila"]
        c = clave["columna"]
        tipo = clave["tipo_de_clave"]
        valor = clave["clave"]

        pos = (f, c)
        if pos not in casillas:
            casillas[pos] = {}

        casillas[pos][tipo] = valor

    for (f, c), tipos in casillas.items():
        x1 = (c - 1) * TAM_CELDA
        y1 = (f - 1) * TAM_CELDA
        x2 = x1 + TAM_CELDA
        y2 = y1 + TAM_CELDA

        # Casilla clave con fondo gris oscuro
        canvas.create_rectangle(x1, y1, x2, y2, fill="gray25", outline="black")

        # Dibujar clave vertical ("C") arriba a la izquierda
        if "C" in tipos and tipos["C"] != 0:
            canvas.create_text(x1 + 5, y1 + 5, text=str(tipos["C"]), anchor="nw", fill="white", font=("Arial", 9, "bold"))

        # Dibujar clave horizontal ("F") abajo a la derecha
        if "F" in tipos and tipos["F"] != 0:
            canvas.create_text(x2 - 5, y2 - 5, text=str(tipos["F"]), anchor="se", fill="white", font=("Arial", 9, "bold"))
#Interfax grafica del juego
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
    partida = cargar_partida()
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
    dibujar_claves_y_casillas(canvas, partida["claves"])

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

    btn_cancel = tk.Button(frame_botones,text = "Volver",command= jueg.destroy,width=12, bg="red")
    btn_cancel.grid(row=0, column=3,pady=5,padx=5)
    
#Interfaz grafica principal.
kaku = tk.Tk()

kaku.title("Menú principal - Kakuro")#Titulo de la ventana

kaku.geometry("600x400")#Vista de la ventana, ancho x alto


menubar = tk.Menu(kaku)
kaku.config(menu=menubar)


filemenu = tk.Menu(menubar, tearoff=0)

menubar.add_command(label="Jugar",command=juego)


menubar.add_command(label="Configuración",command= configura)
menubar.add_command(label = "Acerca de")


menubar.add_command(label = "Ayuda")
menubar.add_command(label = "Cerrar", command= kaku.destroy)


kaku.mainloop()
