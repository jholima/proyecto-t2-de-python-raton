
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


print("--- LABERINTO ORIGINAL ---")
for fila in laberinto:
    print(fila)


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


visitados = []


mov_f = [-1, 0, 1, 0]
mov_c = [0, 1, 0, -1]

puntos_totales = 0
exito = False

def buscar(f, c, puntos):
    global exito, puntos_totales

    if f < 0 or f >= 9 or c < 0 or c >= 9:
        return False

    if laberinto[f][c] == 0:
        return False
    if (f, c) in visitados:
        return False

    valor_celda = laberinto[f][c]
    puntos_actuales = puntos

    if valor_celda == 'I' or valor_celda == 'F':
        puntos_actuales = puntos_actuales + 1
    else:
        puntos_actuales = puntos_actuales + valor_celda

    visitados.append((f, c))

    if f == 0 and c == 0:
        if puntos_actuales >= 23:
            puntos_totales = puntos_actuales
            exito = True
            return True
        else:
            visitados.pop()
            return False

    for i in range(4):
        nueva_f = f + mov_f[i]
        nueva_c = c + mov_c[i]

        if buscar(nueva_f, nueva_c, puntos_actuales):
            return True

    visitados.pop()
    return False

buscar(8, 0, 0)

print("\n--------------------------------")

if exito == True:
    print("El raton logro salir con " + str(puntos_totales) + " puntos!")
    
git add .
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