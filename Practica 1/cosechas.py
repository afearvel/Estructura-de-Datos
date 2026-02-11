cosechas = [12, 24, 16, 15, 20, 18, 6, 10, 12, 14,15, 12]

suma = 0

for x in cosechas:
    suma += x

promedio = suma / len(cosechas)

mayores=[]
menores=[]

for i in cosechas:
    if i > promedio:
        mayores.append(i)
    else: 
        i < promedio
        menores.append(i)
        


print("El promedio de cosechas anual es:", promedio)
print("Cosechas por debajo del promedio:", menores)
print("Cosechas por encima del promedio:", mayores)
