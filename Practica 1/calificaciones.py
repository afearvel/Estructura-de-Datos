cal_alumnos = [8, 8, 7, 5, 10, 9, 9, 5, 6, 10]

suma = 0

for x in cal_alumnos:
    suma += x

promedio = suma / len(cal_alumnos)

aprobados=0
reprobados=0
cal_mayor=0

for cal in cal_alumnos:
    if cal >= 8 and cal <=10:
        cal_mayor += 1

for cal in cal_alumnos:
    if cal <= 5:
        aprobados += 1
    else:
        reprobados += 1

porcentaje = (aprobados / len(cal_alumnos)) * 100


print("El promedio de las calificaciones es:", promedio)
print("El numero de alumnos aprobados es:", aprobados)
print("El numero de alumnos reprobados es:", reprobados)
print("El porcentaje de alumnos aprobados es:", porcentaje, "%")
print("El numero de calificaciones mayores a 8 es:", cal_mayor)
