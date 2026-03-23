dulces = [12500.5, 11890.0, 13010.35, 14100.0, 13650.8, 14999.99, 15800.0, 16250.25, 15120.0, 14780.4, 13999.0, 15550.75]



class Cola:
    def __init__(self):
        self.datos = []

    def enqueue(self, dato):
        self.datos.append(dato)

    def dequeue(self):
        if not self.is_empty():
            return self.datos.pop(0)

    def is_empty(self):
        return len(self.datos) == 0

class Pila:
    def __init__(self):
        self.datos = []

    def push(self, dato):
        self.datos.append(dato)

    def pop(self):
        return self.datos.pop()

    def peek(self):
        return self.datos[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.datos) == 0



def ordenados(lista):
    cola = Cola()
    pila = Pila()

    for i in lista:
        cola.enqueue(i)

    while not cola.is_empty():
        candidato = cola.dequeue()
        es_menor = True

        for j in range(len(cola.datos)):
            candidato2 = cola.dequeue()

            if candidato > candidato2:
                es_menor = False

            cola.enqueue(candidato2)

        if es_menor:
            pila.push(candidato)
        else:
            cola.enqueue(candidato)

    return pila


# Ejecutar
pila_ordenada = ordenados(dulces)

print("Pila ordenada:")
while not pila_ordenada.is_empty():
    print(pila_ordenada.pop())