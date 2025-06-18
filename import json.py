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
        {
            "tipo_de_clave": "F",
            "fila": 2,
            "columna": 1,
            "clave": 10,
            "casillas": 3
        },
        {
            "tipo_de_clave": "C",
            "fila": 1,
            "columna": 2,
            "clave": 15,
            "casillas": 4
        }
    ]
}
partidas.append(nueva_partida)

# Guardar de nuevo
with open(archivo, "w") as f:
    json.dump(partidas, f, indent=4)
