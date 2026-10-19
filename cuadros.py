# Laberinto del examen
# I = inicio, F = fin
laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

# Imprimir laberinto original primero
print("--- LABERINTO ORIGINAL ---")
for fila in laberinto:
    print(fila)

# Matriz para guardar el camino
camino = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

# Lista para no repetir casillas
visitados = []

# Movimientos: Arriba, Derecha, Abajo, Izquierda
mov_f = [-1, 0, 1, 0]
mov_c = [0, 1, 0, -1]

puntos_totales = 0
exito = False

def buscar(f, c, puntos):
    global exito, puntos_totales

    # Verificar si nos salimos del mapa
    if f < 0 or f >= 9 or c < 0 or c >= 9:
        return False

    # Verificar si es pared o si ya pasamos por aqui
    if laberinto[f][c] == 0:
        return False
    if (f, c) in visitados:
        return False

    # Calcular puntos de esta celda
    valor_celda = laberinto[f][c]
    puntos_actuales = puntos

    if valor_celda == 'I' or valor_celda == 'F':
        puntos_actuales = puntos_actuales + 1
    else:
        puntos_actuales = puntos_actuales + valor_celda

    # Guardar celda visitada
    visitados.append((f, c))

    # Verificar si llegamos al final ('F' esta en fila 0, columna 0)
    if f == 0 and c == 0:
        if puntos_actuales >= 23:
            puntos_totales = puntos_actuales
            exito = True
            return True
        else:
            # Si no suma 23 puntos no sirve
            visitados.pop()
            return False

    # Probar los 4 movimientos en orden: Arriba, Derecha, Abajo, Izquierda
    for i in range(4):
        nueva_f = f + mov_f[i]
        nueva_c = c + mov_c[i]

        if buscar(nueva_f, nueva_c, puntos_actuales):
            return True

    # Si ninguno sirvio, borramos esta casilla (backtracking)
    visitados.pop()
    return False

# El raton empieza en la esquina inferior izquierda: fila 8, columna 0 ('I')
buscar(8, 0, 0)

print("\n--------------------------------")

if exito == True:
    print("El raton logro salir con " + str(puntos_totales) + " puntos!")
    
    # Marcamos las casillas del camino con un asterisco *
    for pos in visitados:
        rf = pos[0]
        rc = pos[1]
        if laberinto[rf][rc] != 'I' and laberinto[rf][rc] != 'F':
            camino[rf][rc] = '*'

    print("\n--- MATRIZ CON LA SALIDA ---")
    for fila in camino:
        print(fila)
else:
    print("El raton NO logro salir con los puntos necesarios.")