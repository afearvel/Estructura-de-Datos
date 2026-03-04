class BiCola:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.head = 0
        self.tail = 0
        self.contador = 0

    def is_empty(self):
        return self.contador == 0

    def is_full(self):
        return self.contador == self.capacidad

    def size(self):
        return self.contador

    def enqueue_final(self, elemento):
        if self.is_full():
            return
        self.datos[self.tail] = elemento
        self.tail = (self.tail + 1) % self.capacidad
        self.contador += 1

    def enqueue_frente(self, elemento):
        if self.is_full():
            return
        self.head = (self.head - 1) % self.capacidad
        self.datos[self.head] = elemento
        self.contador += 1

    def dequeue_frente(self):
        if self.is_empty():
            return None
        elemento = self.datos[self.head]
        self.head = (self.head + 1) % self.capacidad
        self.contador -= 1
        return elemento

    def peek_frente(self):
        if self.is_empty():
            return None
        return self.datos[self.head]

    def mostrar(self):
        elementos = []
        i = self.head
        for _ in range(self.contador):
            elementos.append(self.datos[i])
            i = (i + 1) % self.capacidad
        return elementos


# =============================
# FUNCION RETIRO
# =============================

def aplicar_retiro(saldos: BiCola, monto: int, historial: BiCola):
    saldo_original = saldos.dequeue_frente()

    if historial is not None:
        historial.enqueue_frente(f"-{monto}")

    nuevo_saldo = saldo_original - monto
    saldos.enqueue_final(nuevo_saldo)


# =============================
# PROGRAMA PRINCIPAL
# =============================

saldos = BiCola(10)
historial = BiCola(20)

# saldos iniciales
for _ in range(5):
    saldos.enqueue_final(1000)

# lista de retiros distintos
retiros = [500, 400, 300, 200, 100]

# aplicar cada retiro
for monto in retiros:
    aplicar_retiro(saldos, monto, historial)

print("Historial:", historial.mostrar())
print("Saldos finales:", saldos.mostrar())
print("Saldo actual al frente:", saldos.peek_frente())
print("Tamaño del historial:", historial.size())