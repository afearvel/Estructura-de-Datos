from collections import deque

cola = deque(maxlen=3)
limite = 10
tiempo = [0,2,4,6,12]

for x in tiempo:
    print("\nllega:", x)

    #en 10 segundos se vacía toda la cola
    if cola and x - cola[0] >= limite:
        while cola:
            print("dequeue:", cola.popleft())

    #si la cola esta llena sacar el viejo
    elif len(cola) == cola.maxlen:
        print("dequeue:", cola.popleft())

    #enqueue
    cola.append(x)
    print("enqueue:", x)

    #mostrar la cola
    print("cola:", list(cola))