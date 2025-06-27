import json
archivo = "kakuro2025_partidas.json"

# Cargar datos existentes
with open(archivo, "r") as f:
    partidas = json.load(f)
for partida in partidas[:]:
    if partida["nivel_de_dificultad"]== "FÁCIL" and partida["partida"]==2:
        partidas.remove(partida)
# Nueva partida a agregar

with open(archivo, "w") as f:
    json.dump(partidas, f, indent=4)
