palabra = "Parangaricutirimicuaro"

letras = list(palabra)
usadas = []

for l in letras:
    if l not in usadas:
        usadas.append(l)
        print(l, "=", letras.count(l), "es", 
              "MAYUSCULA" if l.isupper() 
              else "minuscula")