from collections import deque

def enqueue(q: deque, elemento) -> None:
    q.append(elemento)

def dequeue(q: deque):
    return q.popleft()

def peek(q: deque):
    return q[0]

def is_empty(q: deque) -> bool:
    return not q

def size(q: deque) -> int:
    return len(q)

def aplicar_retiro(saldo: deque, monto: int, historial: deque) -> None:
    saldo_original = dequeue(saldo)

    if historial is not None:
        enqueue(historial, saldo_original)

    nuevo_saldo = saldo_original - monto
    enqueue(saldo, nuevo_saldo)

def aplicar_deposito(saldo: deque, monto: int, historial: deque) -> None:
    saldo_original = dequeue(saldo)

    if historial is not None:
        enqueue(historial, saldo_original)

    nuevo_saldo = saldo_original + monto
    enqueue(saldo, nuevo_saldo)

# ---

saldos = deque()
historial_retiros = deque()

for _ in range(5):
    enqueue(saldos, 1000)

monto_retiro = 500
monto_deposito = 300

#retiros
for _ in range(5):
    aplicar_retiro(saldos, monto_retiro, historial_retiros)

#depósitos
for _ in range(5):
    aplicar_deposito(saldos, monto_deposito, None)

print("Historial de retiros:", list(historial_retiros))
print("Saldos finales:", list(saldos))


