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

    def dequeue_final(self):
        if self.is_empty():
            return None
        self.tail = (self.tail - 1) % self.capacidad
        elemento = self.datos[self.tail]
        self.contador -= 1
        return elemento

    def peek_frente(self):
        if self.is_empty():
            return None
        return self.datos[self.head]

    def peek_final(self):
        if self.is_empty():
            return None
        return self.datos[(self.tail - 1) % self.capacidad]

    def mostrar(self):
        elementos = []
        i = self.head
        for _ in range(self.contador):
            elementos.append(self.datos[i])
            i = (i + 1) % self.capacidad
        return elementos


# =============================
# FUNCIONES DEL BANCO
# =============================

def aplicar_retiro(saldos: BiCola, monto: int, historial: BiCola):
    saldo_original = saldos.dequeue_frente()

    if historial is not None:
        historial.enqueue_frente(saldo_original)  # head = retiros

    nuevo_saldo = saldo_original - monto
    saldos.enqueue_final(nuevo_saldo)


def aplicar_deposito(saldos: BiCola, monto: int, historial: BiCola):
    saldo_original = saldos.dequeue_frente()

    if historial is not None:
        historial.enqueue_final(saldo_original)  # tail = depósitos

    nuevo_saldo = saldo_original + monto
    saldos.enqueue_final(nuevo_saldo)


# =============================
# PROGRAMA PRINCIPAL
# =============================

saldos = BiCola(10)
historial = BiCola(20)

for _ in range(5):
    saldos.enqueue_final(1000)

monto_retiro = 500
monto_deposito = 300

for _ in range(5):
    aplicar_retiro(saldos, monto_retiro, historial)

for _ in range(5):
    aplicar_deposito(saldos, monto_deposito, historial)

print("Historial:", historial.mostrar())
print("Saldos finales:", saldos.mostrar())
print("Saldo actual:", saldos.peek_frente())
print("Tamaño del historial:", historial.size())