import io, sys 

def run_calificaciones(calificaciones_input=None):
    cal_alumnos = calificaciones_input or [8, 8, 7, 5, 10, 9, 9, 5, 6, 10]
    suma = sum(cal_alumnos)
    promedio = suma / len(cal_alumnos)
    aprobados = sum(1 for c in cal_alumnos if c > 5)
    reprobados = sum(1 for c in cal_alumnos if c <= 5)
    cal_mayor = sum(1 for c in cal_alumnos if 8 <= c <= 10)
    porcentaje = (aprobados / len(cal_alumnos)) * 100
    return {
        "calificaciones": cal_alumnos,
        "promedio": round(promedio, 2),
        "aprobados": aprobados,
        "reprobados": reprobados,
        "porcentaje": round(porcentaje, 2),
        "mayores_8": cal_mayor
    }

def run_cosechas(cosechas_input=None):
    cosechas = cosechas_input or [12, 24, 16, 15, 20, 18, 6, 10, 12, 14, 15, 12]
    promedio = sum(cosechas) / len(cosechas)
    mayores = [i for i in cosechas if i > promedio]
    menores = [i for i in cosechas if i <= promedio]
    return {
        "cosechas": cosechas,
        "promedio": round(promedio, 2),
        "mayores": mayores,
        "menores": menores
    }

def run_numrepetidos(numeros_input=None):
    numeros = numeros_input or [1,2,4,4,4,5,7,9,11,11,13,14,15,16,16]
    repetidos = []
    previo = None
    numeros_nuevos = []
    registrados = []
    for num in numeros:
        if num == previo and num not in repetidos:
            repetidos.append(num)
        previo = num
        if num not in registrados:
            numeros_nuevos.append(num)
            registrados.append(num)
    return {
        "numeros": numeros,
        "repetidos": repetidos,
        "sin_repetidos": numeros_nuevos
    }

def run_palabras(palabra_input=None):
    palabra = palabra_input or "Parangaricutirimicuaro"
    letras = list(palabra)
    usadas = []
    resultado = []
    for l in letras:
        if l not in usadas:
            usadas.append(l)
            resultado.append({
                "letra": l,
                "count": letras.count(l),
                "tipo": "MAYÚSCULA" if l.isupper() else "minúscula"
            })
    return {"palabra": palabra, "letras": resultado}

def run_palabrasnoarr(palabra_input=None):
    palabra = palabra_input or "Parangaricutirimicuaro"
    conteo = {}
    mayusculas = {}
    for l in palabra:
        key = l.lower()
        conteo[key] = conteo.get(key, 0) + 1
        if l.isupper():
            mayusculas[key] = True
    resultado = []
    for k, v in conteo.items():
        resultado.append({
            "letra": k.upper() if mayusculas.get(k) else k,
            "count": v,
            "es_mayuscula": mayusculas.get(k, False)
        })
    return {"palabra": palabra, "letras": resultado}
