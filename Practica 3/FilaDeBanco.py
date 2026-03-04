def enque(lista, elemento):
    lista.append(elemento)

def deque(lista):
    return lista.pop(0)

def peek(lista):
    return lista[0]

def is_empty(lista):
    if lista == []:
        return True
    else:
        return False
    
def size(lista):
    return len(lista)
 

saldo = [1000, 1000, 1000, 1000, 1000]
retiros = []
depositos = []



def retirarDinero(saldo, cantidad):
    saldo_actual = peek(saldo)
    deque(saldo)
    if saldo_actual >= cantidad:
        saldo_actual -= cantidad
        enque(retiros, cantidad)
        print("Retiro realizado, saldo:", saldo_actual)
    else:
        print("Saldo insuficiente.")
    enque(saldo, saldo_actual)

def depositarDinero(saldo, cantidad):
    saldo_actual = peek(saldo)
    deque(saldo)
    saldo_actual += cantidad
    enque(depositos, cantidad)
    print("Deposito realizado, saldo:", saldo_actual)
    enque(saldo, saldo_actual)

print("Saldos:", saldo)


for _ in range(size(saldo)):
    retirarDinero(saldo, 500)
    
for _ in range(size(saldo)):
    depositarDinero(saldo, 300)

print("\nSaldos finales:", saldo)
print("Historial de retiros:", retiros)
print("Historial de depósitos:", depositos)