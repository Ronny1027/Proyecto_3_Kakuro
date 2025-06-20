import json
archivo = "kakuro2025_partidas.json"

# Cargar datos existentes
with open(archivo, "r") as f:
    partidas = json.load(f)

# Nueva partida a agregar
nueva_partida = {
    "nivel_de_dificultad": "FÁCIL",
    "partida": 1,
    "claves": [
        {"tipo_de_clave": "F", "fila": 1, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 1, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 1, "columna": 2, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 1, "columna": 2, "clave": 16, "casillas": 2},
        {"tipo_de_clave": "F", "fila": 1, "columna": 3, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 1, "columna": 3, "clave": 38, "casillas": 8},
        {"tipo_de_clave": "F", "fila": 1, "columna": 4, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 1, "columna": 4, "clave": 0, "casillas":8},
        {"tipo_de_clave": "F", "fila": 1, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 1, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 1, "columna": 6, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 1, "columna": 6, "clave": 0, "casillas":2},
        {"tipo_de_clave": "F", "fila": 1, "columna": 7, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 1, "columna": 7, "clave": 11, "casillas": 4},
        {"tipo_de_clave": "F", "fila": 1, "columna": 8, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 1, "columna": 8, "clave": 38, "casillas": 8},
        {"tipo_de_clave": "F", "fila": 1, "columna": 9, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 1, "columna": 9, "clave": 0, "casillas": 0},
        
        {"tipo_de_clave": "F", "fila": 2, "columna": 1, "clave": 16, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 2, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 2, "columna": 4, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 2, "columna": 4, "clave": 16, "casillas": 2},
        {"tipo_de_clave": "F", "fila": 2, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 2, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 2, "columna": 6, "clave": 7, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 2, "columna": 6, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 2, "columna": 9, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 2, "columna": 9, "clave": 0, "casillas": 0},
        
        
        {"tipo_de_clave": "F", "fila": 3, "columna": 1, "clave": 18, "casillas": 3},
        {"tipo_de_clave": "C", "fila": 3, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 3, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 3, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 3, "columna": 6, "clave": 14, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 3, "columna": 6, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 3, "columna": 9, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 3, "columna": 9, "clave": 0, "casillas": 0},

        {"tipo_de_clave": "F", "fila": 4, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 4, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 4, "columna": 2, "clave": 13, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 4, "columna": 2, "clave": 13, "casillas": 2},
        {"tipo_de_clave": "F", "fila": 4, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 4, "columna": 5, "clave": 13, "casillas": 2},
        {"tipo_de_clave": "F", "fila": 4, "columna": 6, "clave": 4, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 4, "columna": 6, "clave": 17, "casillas": 2},
        {"tipo_de_clave": "F", "fila": 4, "columna": 9, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 4, "columna": 9, "clave": 3, "casillas": 2},
        
        {"tipo_de_clave": "F", "fila": 5, "columna": 1, "clave": 17, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 5, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 5, "columna": 4, "clave": 24, "casillas": 5},
        {"tipo_de_clave": "C", "fila": 5, "columna": 4, "clave": 18, "casillas": 4},
     

        {"tipo_de_clave": "F", "fila": 6, "columna": 1, "clave": 34, "casillas": 5},
        {"tipo_de_clave": "C", "fila": 6, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 6, "columna": 7, "clave": 3, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 6, "columna": 7, "clave": 16, "casillas": 2},
   

        {"tipo_de_clave": "F", "fila": 7, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 7, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 7, "columna": 2, "clave": 3, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 7, "columna": 2, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 7, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 7, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 7, "columna": 6, "clave": 15, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 7, "columna": 6, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 7, "columna": 9, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 7, "columna": 9, "clave": 10, "casillas": 2},
        
        {"tipo_de_clave": "F", "fila": 8, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 8, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 8, "columna": 2, "clave": 4, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 8, "columna": 2, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 8, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 8, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 8, "columna": 6, "clave": 23, "casillas": 3},
        {"tipo_de_clave": "C", "fila": 8, "columna": 6, "clave": 0, "casillas": 0},

        {"tipo_de_clave": "F", "fila": 9, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 9, "columna": 1, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 9, "columna": 2, "clave": 11, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 9, "columna": 2, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 9, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 9, "columna": 5, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 9, "columna": 6, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "C", "fila": 9, "columna": 6, "clave": 0, "casillas": 0},
        {"tipo_de_clave": "F", "fila": 9, "columna": 7, "clave": 3, "casillas": 2},
        {"tipo_de_clave": "C", "fila": 9, "columna": 7, "clave": 0, "casillas": 0},
    ]
}


partidas.append(nueva_partida)

# Guardar de nuevo
with open(archivo, "w") as f:
    json.dump(partidas, f, indent=4)
