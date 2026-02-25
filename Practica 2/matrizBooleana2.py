Asientos = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

def coordenadasValidas(F, C):
    return 0 <= F < len(Asientos) and 0 <= C < len(Asientos[0])


def reservar(F, C):
    if not coordenadasValidas(F, C):
        return "Coordenadas invalidas"

    if Asientos[F][C] == 1:
        return "Ocupado"

    Asientos[F][C] = 1
    return "Reservado"


def liberar(F, C):
    if not coordenadasValidas(F, C):
        return "Coordenadas invalidas"

    if Asientos[F][C] == 0:
        return "Ya libre"

    Asientos[F][C] = 0
    return "Liberado"


def consultar(F, C):
    if not coordenadasValidas(F, C):
        return "Coordenadas invalidas"

    if Asientos[F][C] == 1:
        return "Reservado"
    else:
        return "Libre"


def operaciones(op, F, C):
    if op == "RESERVAR":
        return reservar(F, C)
    elif op == "LIBERAR":
        return liberar(F, C)
    elif op == "CONSULTAR":
        return consultar(F, C)
    
#-------------------------------------------

pruebas = [
    ("RESERVAR", 1, 1),
    ("RESERVAR", 1, 2),
    ("RESERVAR", 1, 1),
    ("CONSULTAR", 1, 1),
    ("LIBERAR", 1, 1),
    ("LIBERAR", 1, 1),
    ("RESERVAR", 3, 4),
    ("RESERVAR", 6, 6),
    ("CONSULTAR", 6, 6),
    ("RESERVAR", 2, 5)
]

for op, f, c in pruebas:
    print(operaciones(op, f-1, c-1,))


#total reservados
total = 0

for fila in Asientos:
    for a in fila:
        if a == 1:
            total += 1
print("Total reservados:", total)


#mayor reservados
mayor = -1
fila_max = 0

for i in range(len(Asientos)):

    cont = 0
    for a in Asientos[i]:
        if a == 1:
            cont += 1

    if cont > mayor:
        mayor = cont
        fila_max = i + 1
print("Fila con más reservados:", fila_max)