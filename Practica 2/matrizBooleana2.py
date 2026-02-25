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