import pandas as pd

def media(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma/len(lista)

def moda(lista):
    conteo = {}
    moda = lista[0]
    contador = 0

    for num in lista:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1

        if conteo[num] > contador:
            contador = conteo[num]
            moda = num

    return moda

def varianza(lista, mediaV):
    suma = 0
    for i in lista:
        suma += (i - mediaV) ** 2
    return suma / len(lista)

def desviacion_estandar(varianzaV):
    return varianzaV ** 0.5



df = pd.read_csv("Practica 2/Housing.csv")

columnas = ["price","bedrooms","bathrooms","sqft_living","sqft_lot","floors","sqft_above","sqft_basement","yr_built"]

for col in columnas:
    lista = list(df[col])

    m = media(lista)
    mo = moda(lista)
    v = varianza(lista, m)
    d = desviacion_estandar(v)

    print(f"\nColumna: {col}")
    print("Media:", m)
    print("Moda:", mo)
    print("Varianza:", v)
    print("Desviación estándar:", d)