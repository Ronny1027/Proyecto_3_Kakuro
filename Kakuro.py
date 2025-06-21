#Modulos o importaciones necesarias para el programa.
import tkinter as tk


#Para emitir errores.
from tkinter import messagebox

#Para manipular archivos de información.
import json
#Para seleccionar partida aleatoria
import random

#Cargar las partidas de juego
partidas_usa = []
def cargar_partida():
    global partidas_usa
    with open("kakuro2025_partidas.json","r") as w:
        partidas = json.load(w)
    with open("kakuro2025_configuración","r") as r:
        confi = json.load(r)
    difi = confi["Nivel"]
    partida_dispo = []
    restantes = []
    for partida in partidas:
        if partida["nivel_de_dificultad"]== difi:
            partida_dispo.append(partida)
    if len(partidas_usa) >= len(partida_dispo):
        partidas_usa = []
    for p in partida_dispo:
        if p not in partidas_usa:
            restantes.append(p)
    parti_selec = random.choice(restantes)
    partidas_usa.append(parti_selec)
    return parti_selec
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
    tk.Radiobutton(frame_nive, text="Fácil", variable=difi_var, value="FÁCIL").pack(anchor="w", padx=20)
    tk.Radiobutton(frame_nive, text="Medio", variable=difi_var, value="MEDIO").pack(anchor="w", padx=20)
    tk.Radiobutton(frame_nive, text="Difícil", variable=difi_var, value="DIFÍCIL").pack(anchor="w", padx=20)
    tk.Radiobutton(frame_nive, text="Experto", variable=difi_var, value="EXPERTO").pack(anchor="w", padx=20)
    
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
    label_tempo = tk.Label(frame_tempo, text="Indique el tiempo(en caso de elegir temporizador)")
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
        global partidas_usa
        partidas_usa = []#se reinicia la variable en caso de cambiar la dificultad.
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
#Funciones para el kakuro
#Variables necesarias para el proceso de juego
numero_selec = None
entrada_casillas = {}
boton_act = None
casi_selec = None
pila_desh = []
pila_reha= []
jugadas = {}
#Función para deshacer una jugada
def deshacer_jugada():
    if pila_desh == []:
        messagebox.showerror("Error", "No hay jugadas para deshacer.")
        return
    info = pila_desh.pop()
    fila = info[0]
    col = info[1]
    valo_ante = info[2]
    valor_act = info[3]#se accede a cada elemento de la información de la pila.

    entry = entrada_casillas[(fila, col)]#Se obtiene la ubicación
    entry.config(state="normal")
    entry.delete(0, tk.END)
    if valo_ante != "":
        entry.insert(0, valo_ante)
        jugadas[(fila, col)] = valo_ante
    else:
        if (fila, col) in jugadas:
            del jugadas[(fila, col)]
    entry.config(state="readonly")
    pila_reha.append((fila, col, valo_ante, valor_act))#El orden de los valores cambia

#Función para rehacer una jugada.
def rehacer_jugada():
    if pila_reha == []:
        messagebox.showerror("Error", "No hay jugadas para rehacer.")
        return
    info2 = pila_reha.pop()
    fila = info2[0]
    col = info2[1]
    valo_ante = info2[2]
    valor_nuev= info2[3]#se accede a cada elemento de la información de la pila.
    entry = entrada_casillas[(fila, col)]#Se obtiene la ubicación

    entry.config(state="normal")
    entry.delete(0, tk.END)
    if valor_nuev != "":
        entry.insert(0, valor_nuev)
        jugadas[(fila, col)] = valor_nuev
    else:
        if (fila, col) in jugadas:
            del jugadas[(fila, col)]
    entry.config(state="readonly")
    pila_desh.append((fila, col, valo_ante, valor_nuev))
                 
#Función para quitarle el color verde al boton
def deseleccionar_botones():
    global boton_act
    if boton_act!= None:
        boton_act.config(bg="SystemButtonFace")
        boton_act = None
#Función para validar la información de la jugada.
def es_jugada_valida(fila, col, valor):
    for (f, c), v in jugadas.items():
        if f == fila and v == valor:
            messagebox.showerror("Error", f"Ya existe el número {valor} en la fila")
            return False
        if c == col and v == valor:
            messagebox.showerror("Error", f"Ya existe el número {valor} en la columna")
            return False
    return True

#Función para poder colocar el número con las coordenadas
def colocar_numero(entry_widget, fila, col):
    global numero_selec
    global casi_selec
    if numero_selec is None:
        messagebox.showerror("Error", "Debe seleccionar un número")
        return
    cont_actual = entry_widget.get()
    if cont_actual != "":
        messagebox.showerror("Error", "Ya hay un número en esa casilla")
        return
    #Validación de jugada valida
    if not es_jugada_valida(fila, col, numero_selec):
        return
    valo_ante = entry_widget.get()
    pila_desh.append((fila, col, valo_ante, numero_selec))
    pila_reha.clear()

    entry_widget.config(state="normal")#Se pone el estado editable
    entry_widget.insert(0, str(numero_selec))#Se inserta el número
    entry_widget.config(state="readonly")#Se vuelve a poner el estado ineditable

    jugadas[(fila, col)] = numero_selec#se guarda la información de la jugada
    casi_selec = entry_widget
    deseleccionar_botones()  #Quitar el color despues del proceso
    numero_selec = None#Se reinicia el valor
#Función para poner el boton en verde.
def seleccionar_numero(n, boton):
    global numero_selec
    global boton_act
    numero_selec = n#El numero pasa a ser el valor del boton
    if boton_act != None:#Si se presiona el botón
        boton_act.config(bg="SystemButtonFace")  # Reinicar boton anterior
    boton_act = boton#El boton pasa a tener un nuevo valor
    boton_act.config(bg="green")
#Función para hacer el proceso de borrar el número de una casilla.
def borrar_casi():
    global casi_selec
    if casi_selec == None:
        messagebox.showerror("Error", "Debe seleccionar una casilla")
        return
    casi_selec.config(state="normal")#Para poder editar la casilla
    casi_selec.delete(0, tk.END)
    casi_selec.config(state="readonly")
    casi_selec = None#se reinicia el valor
#Poner los entry en las casillas jugables.
def crear_casillas_jugables(canvas, claves, frame_tablero):
    jugables = set()
    usadas = {(clave["fila"], clave["columna"]) for clave in claves}
    for fila in range(1, FILAS + 1):
        for col in range(1, COLUMNAS + 1):
            if (fila, col) not in usadas:
                x1 = (col - 1) * TAM_CELDA
                y1 = (fila - 1) * TAM_CELDA
                entry = tk.Entry(canvas, width=2, justify='center', font=("Arial", 12), state="readonly")
                canvas.create_window(x1 + TAM_CELDA // 2, y1 + TAM_CELDA // 2, window=entry, width=25, height=25)
                entry.bind("<Button-1>", lambda event, fila=fila, col=col: colocar_numero(event.widget, fila, col))
                entrada_casillas[(fila, col)] = entry
#Dibujar la cuadricula
def dibujar_claves_y_casillas(canvas, claves,):
    casillas = {}
    usadas = set()
    for clave in claves:
        f = clave["fila"]
        c = clave["columna"]
        tipo = clave["tipo_de_clave"]
        valor = clave["clave"]
        pos = (f, c)
        usadas.add(pos)
        if pos not in casillas:
            casillas[pos] = {}

        casillas[pos][tipo] = valor
    for fila in range(1, FILAS + 1):
        for col in range(1, COLUMNAS + 1):
            x1 = (col - 1) * TAM_CELDA
            y1 = (fila - 1) * TAM_CELDA
            x2 = x1 + TAM_CELDA
            y2 = y1 + TAM_CELDA
            pos = (fila, col)
            if pos in casillas:
                canvas.create_rectangle(x1, y1, x2, y2, fill="gray25", outline="black")
                tipos = casillas[pos]
                if (tipos.get("F", 0) != 0) or (tipos.get("C", 0) != 0):
                    canvas.create_line(x1, y1, x2, y2, fill="white")
                if "C" in tipos and tipos["C"] != 0:
                    canvas.create_text(x1 + 5, y2 - 5, text=str(tipos["C"]), anchor="sw", fill="white", font=("Arial", 9, "bold"))
                if "F" in tipos and tipos["F"] != 0:
                    canvas.create_text(x2 - 5, y1 + 5, text=str(tipos["F"]), anchor="ne", fill="white", font=("Arial", 9, "bold"))
#Funciones de juego(no graficas)
def ini_relo():
    global tiemp_relo
    global tipo_relo
    global id_relo
def iniciar_juego(nom,tiemp):
    if nom =="":
        messagebox.showerror("Error", "Digite su nombre")
        return
    if len(nom)>40 :
        messagebox.showerror("Error", "Digite un nombre valido")
        return
    crear_casillas_jugables(canvas, partida["claves"], frame_tablero)


#Interfaz grafica del juego
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
    global canvas
    global partida
    global frame_tablero
    partida = cargar_partida()#Valor aleatorio del json
    jueg = tk.Toplevel(kaku)
    jueg.title("Jugar Kakuro")
    jueg.geometry("700x600")
    #Frame general para acomodar los frames.
    frame_principal = tk.Frame(jueg)
    frame_principal.pack(padx=10, pady=10)

    #Frame para agrupar los elementos de la izquierda.
    frame_tablero = tk.Frame(frame_principal)
    frame_tablero.grid(row=0, column=0, padx=5)

    lbl_titulo = tk.Label(frame_tablero, text="KAKURO", font=("Helvetica", 16, "bold"))
    lbl_titulo.grid(row=0, column=0, pady=(0, 10))
    #Se obtiene la cuadricula de las funciones que estan
    ancho_canvas = COLUMNAS * TAM_CELDA + 1
    alto_canvas = FILAS * TAM_CELDA + 1
    canvas = tk.Canvas(frame_tablero, width=ancho_canvas, height=alto_canvas, bg="white", highlightthickness=0)
    canvas.grid(row=1, column=0)
    dibujar_cuadricula(canvas)
    dibujar_claves_y_casillas(canvas, partida["claves"])

    

    lbl_reloj = tk.Label(frame_tablero, text="Reloj:", font=("Arial", 10))
    lbl_reloj.grid(row=3, column=0, pady=(10, 0))

    entry_reloj = tk.Entry(frame_tablero, width=10, justify="center", font=("Courier", 12))
    entry_reloj.grid(row=4, column=0, pady=(0, 10))

    with open("kakuro2025_configuración","r") as w:
        confi = json.load(w)
    dificul = confi["Nivel"]
    relo = confi["Reloj"]
    tempo = confi["Temporizador"]
    if relo == "tempori":
        if tempo != "No hay":
            entry_reloj.insert(0,tempo)
    if relo == "crono":
        entry_reloj.insert(0, "00:00:00")

    
    lbl_nivel = tk.Label(frame_tablero, text=f"Nivel: {dificul}", font=("Arial", 11, "italic"))
    lbl_nivel.grid(row=5, column=0, pady=(5, 0))
    #Frame para agrupar las opciones de la derecha(nombre,numeros y botones)
    frame_opciones = tk.Frame(frame_principal)
    frame_opciones.grid(row=0, column=1, padx=20, sticky="n")
    #Subframe del frame_opciones para acomodar todo mejor.
    frame_contenido = tk.Frame(frame_opciones)
    frame_contenido.pack(pady=10, fill="x")

    # Etiqueta de jugador
    tk.Label(frame_contenido, text="Jugador:").pack()
    entry_nom = tk.Entry(frame_contenido, width=25)
    entry_nom.pack(pady=5)
    b = None
    
    btn_ini = tk.Button(frame_tablero, text="Iniciar juego", bg="hotpink",command=lambda: iniciar_juego(entry_nom.get(),entry_reloj.get))
    btn_ini.grid(row=2, column=0, pady=5)
    # Números del 1 al 9
    btn1 = tk.Button(frame_contenido, text="1", width=6, height=1)
    btn1.config(command=lambda: seleccionar_numero(1, btn1))
    btn1.pack(pady=7)
    btn2 = tk.Button(frame_contenido, text="2", width=6, height=1)
    btn2.config(command=lambda: seleccionar_numero(2, btn2))
    btn2.pack(pady=7)
    btn3 = tk.Button(frame_contenido, text="3", width=6, height=1)
    btn3.config(command=lambda: seleccionar_numero(3, btn3))
    btn3.pack(pady=7)
    btn4 = tk.Button(frame_contenido, text="4", width=6, height=1)
    btn4.config(command=lambda: seleccionar_numero(4, btn4))
    btn4.pack(pady=7)
    btn5 = tk.Button(frame_contenido, text="5", width=6, height=1)
    btn5.config(command=lambda: seleccionar_numero(5, btn5))
    btn5.pack(pady=7)
    btn6 = tk.Button(frame_contenido, text="6", width=6, height=1)
    btn6.config(command=lambda: seleccionar_numero(6, btn6))
    btn6.pack(pady=7)
    btn7 = tk.Button(frame_contenido, text="7", width=6, height=1)
    btn7.config(command=lambda: seleccionar_numero(7, btn7))
    btn7.pack(pady=7)
    btn8 = tk.Button(frame_contenido, text="8", width=6, height=1)
    btn8.config(command=lambda: seleccionar_numero(8, btn8))#Configuración aparte para más orden
    btn8.pack(pady=7)
    btn9 = tk.Button(frame_contenido, text="9", width=6, height=1)
    btn9.config(command=lambda: seleccionar_numero(9, btn9))
    btn9.pack(pady=7)
    #Boton especial de borrar
    tk.Button(frame_contenido, text="Borrar", width=6, height=1, bg="red", fg="white", command=lambda: borrar_casi()).pack(pady=5)
    
    #Para agrupar los botones con opciones especiales(iniciar,guardar,etc)
    frame_botones = tk.Frame(frame_opciones)
    frame_botones.pack(pady=10, fill="x")

    btn_desh = tk.Button(frame_botones, text="Deshacer jugada",width=12, bg="lightgreen",command=deshacer_jugada)
    btn_desh.grid(row=0, column=0, pady=5,padx=5)

    btn_reh = tk.Button(frame_botones, text="Rehacer jugada",width=12, bg="lightblue",command=rehacer_jugada)
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
