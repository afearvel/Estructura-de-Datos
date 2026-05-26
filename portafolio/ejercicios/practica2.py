import os, csv

def run_coordenadas(valor=7, matriz=None):
    A = matriz or [
        [4,7,2,9,5,7],[1,3,7,6,8,0],[9,2,5,7,4,6],
        [8,7,1,3,7,2],[5,0,6,4,2,9],[7,8,9,2,1,7]
    ]
    coordenadas = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == valor:
                coordenadas.append([i+1, j+1])
    return {"matriz": A, "valor": valor, "coordenadas": coordenadas}

def run_matrices(A=None, B=None):
    A = A or [[5,6,13],[3,10,1],[2,11,3]]
    B = B or [[1,2,17],[6,5,15],[3,11,12]]
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return {"A": A, "B": B, "C": C}

def run_matriz_booleana(operaciones=None):
    Asientos = [[0]*6 for _ in range(6)]
    ops = operaciones or [
        ("RESERVAR",1,1),("RESERVAR",1,2),("RESERVAR",1,1),
        ("CONSULTAR",1,1),("LIBERAR",1,1),("LIBERAR",1,1),
        ("RESERVAR",3,4),("RESERVAR",6,6),("CONSULTAR",6,6),("RESERVAR",2,5)
    ]
    def valida(f,c): return 0<=f<6 and 0<=c<6
    def reservar(f,c):
        if not valida(f,c): return "Coordenadas inválidas"
        if Asientos[f][c]==1: return "Ocupado"
        Asientos[f][c]=1; return "Reservado"
    def liberar(f,c):
        if not valida(f,c): return "Coordenadas inválidas"
        if Asientos[f][c]==0: return "Ya libre"
        Asientos[f][c]=0; return "Liberado"
    def consultar(f,c):
        if not valida(f,c): return "Coordenadas inválidas"
        return "Reservado" if Asientos[f][c]==1 else "Libre"
    resultados = []
    for op,f,c in ops:
        f0,c0 = f-1,c-1
        if op=="RESERVAR": r=reservar(f0,c0)
        elif op=="LIBERAR": r=liberar(f0,c0)
        else: r=consultar(f0,c0)
        resultados.append({"op":op,"fila":f,"col":c,"resultado":r})
    total = sum(a for fila in Asientos for a in fila)
    mayor=-1; fila_max=0
    for i,fila in enumerate(Asientos):
        cont=sum(fila)
        if cont>mayor: mayor=cont; fila_max=i+1
    return {"operaciones":resultados,"asientos":Asientos,"total":total,"fila_max":fila_max}

def run_dataframe(csv_path=None):
    path = csv_path or os.path.join(os.path.dirname(__file__),'../data/Housing.csv')
    columnas = ["price","bedrooms","bathrooms","sqft_living","sqft_lot","floors","sqft_above","sqft_basement","yr_built"]
    data = {col: [] for col in columnas}
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for col in columnas:
                try: data[col].append(float(row[col]))
                except: pass
    resultados = []
    for col in columnas:
        lista = data[col]
        media = sum(lista)/len(lista)
        conteo={}
        for x in lista:
            conteo[x]=conteo.get(x,0)+1
        moda = max(conteo, key=conteo.get)
        varianza = sum((x-media)**2 for x in lista)/len(lista)
        desv = varianza**0.5
        resultados.append({
            "columna":col,
            "media":round(media,2),
            "moda":round(moda,2),
            "varianza":round(varianza,2),
            "desviacion":round(desv,2)
        })
    return {"resultados": resultados}
