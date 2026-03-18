from collections import deque

cola = deque()

tareas = [
    ["T1",1,0],
    ["T2",0,0],
    ["T3",2,0],
    ["T4",1,0],
    ["T5",2,2],
    ["T6",2,1]
]

# enqueue inicial
for x in tareas:
    cola.append(x)

print("cola inicial:", list(cola))

completadas = 0
n = len(tareas)

while completadas < n:

    tarea = cola.popleft()

    nombre = tarea[0]
    fallos = tarea[1]
    intentos = tarea[2]

    print("\nprocesando:", nombre)

    if fallos > 0:

        print("fallo")

        tarea[1] -= 1
        tarea[2] += 1

        cola.append(tarea)   # se manda al final

        print("append (cola)")

    else:

        print("exito")

        cola.appendleft(tarea)  # se manda al inicio

        completadas += 1

        print("appendleft (cabeza)")

    print("cola:", list(cola))
