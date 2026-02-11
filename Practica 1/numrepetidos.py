numeros = [1,2,4,4,4,5,7,9,11,11,13,14,15,16,16]

repetidos = []
previo = None
    

numeros_nuevos = []
numeros_registrados = []

for num in numeros:
    if num == previo and num not in repetidos:
        repetidos.append(num)
    previo = num
    if num not in numeros_registrados:
        numeros_nuevos.append(num)
        numeros_registrados.append(num)

print("Números repetidos:", repetidos)
print("Números sin repetidos:", numeros_nuevos)