import pandas as pd

df = pd.read_csv("Practica 2/Housing.csv")

columnas = [
    "price",
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "sqft_above",
    "sqft_basement",
    "yr_built"
]

for col in columnas:
    lista = list(df[col])

    # MEDIA
    suma = 0
    for i in lista:
        suma += i
    media = suma / len(lista)

    # MODA
    moda = lista[0]
    max_contador = 0
    for i in lista:
        contador = 0
        for j in lista:
            if i == j:
                contador += 1
        if contador > max_contador:
            max_contador = contador
            moda = i

    # VARIANZA
    suma_varianza = 0
    for i in lista:
        suma_varianza += (i - media) ** 2
    varianza = suma_varianza / len(lista)

    # DESVIACIÓN ESTÁNDAR
    desviacion = varianza ** 0.5

    print(f"\nColumna: {col}")
    print("Media:", media)
    print("Moda:", moda)
    print("Varianza:", varianza)
    print("Desviación estándar:", desviacion)
