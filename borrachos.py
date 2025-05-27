import time
import random

# Acciones posibles y exclusivas
acciones_posibles = ["Tomar cerveza", "Usar baño", "Llamada-Ex", "Cantando", "Bailando"]
acciones_exclusivas = ["Usar baño", "Llamada-Ex"]

# Lista de borrachitos
borrachos = ["Angel", "Zuñiga", "Alan", "Carlos", "Brayan"]

# Ejecutar acciones
def ejecutar_accion(nombre, accion):
    if accion == "Tomar cerveza":
        print(f"{nombre} está tomando cerveza...")
    elif accion == "Usar baño":
        print(f"{nombre} está orinando...")
        time.sleep(1)
        print(f"{nombre} salió del baño.")
    elif accion == "Llamada-Ex":
        print(f"{nombre} está llamadando a su Ex...")
    elif accion == "Cantando":
        print(f"{nombre} está cantando")
    elif accion == "Bailando":
        print(f"{nombre} está bailando")
    time.sleep(1)

# Verifica que acciones exclusivas no se repitan
def obtener_accion_disponible(en_uso):
    while True:
        accion = random.choice(acciones_posibles)
        if accion in acciones_exclusivas and any(a in en_uso for a in acciones_exclusivas):
            continue
        return accion

# Ejecutar 4 ciclos
for ciclo in range(4):
    print(f"\n--- CICLO {ciclo + 1} ---")
    en_uso = []
    acciones_asignadas = []

    for borracho in borrachos:
        accion = obtener_accion_disponible(en_uso)
        acciones_asignadas.append((borracho, accion))
        if accion in acciones_exclusivas:
            en_uso.append(accion)

    for borracho, accion in acciones_asignadas:
        ejecutar_accion(borracho, accion)
