import heapq

# ====== PRACTICA 5: PILAS ======

def run_pilas(lista_input=None):
    dulces = lista_input or [12500.5,11890.0,13010.35,14100.0,13650.8,14999.99,15800.0,16250.25,15120.0,14780.4,13999.0,15550.75]

    class Cola:
        def __init__(self): self.datos=[]
        def enqueue(self,d): self.datos.append(d)
        def dequeue(self):
            if self.datos: return self.datos.pop(0)
        def is_empty(self): return len(self.datos)==0

    class Pila:
        def __init__(self): self.datos=[]
        def push(self,d): self.datos.append(d)
        def pop(self): return self.datos.pop()
        def peek(self): return self.datos[-1] if self.datos else None
        def is_empty(self): return len(self.datos)==0

    cola=Cola(); pila=Pila()
    for i in dulces: cola.enqueue(i)
    while not cola.is_empty():
        candidato=cola.dequeue(); es_menor=True
        for j in range(len(cola.datos)):
            c2=cola.dequeue()
            if candidato>c2: es_menor=False
            cola.enqueue(c2)
        if es_menor: pila.push(candidato)
        else: cola.enqueue(candidato)
    ordenada=[]
    while not pila.is_empty(): ordenada.append(pila.pop())
    return {"lista_original":dulces,"lista_ordenada":list(reversed(ordenada)),"algoritmo":"Ordenamiento con Pila + Cola"}

# ====== PRACTICA 6: ÁRBOLES ======

def run_ejemplo_arbol(datos=None):
    datos = datos or [3,1,4,2,5]

    class Nodo:
        def __init__(self,v): self.valor=v; self.izq=None; self.der=None

    class Arbol:
        def __init__(self): self.raiz=None
        def agregar(self,d):
            if not self.raiz: self.raiz=Nodo(d); return
            self._agregar(self.raiz,d)
        def _agregar(self,n,d):
            if d<n.valor:
                if n.izq is None: n.izq=Nodo(d)
                else: self._agregar(n.izq,d)
            elif d>n.valor:
                if n.der is None: n.der=Nodo(d)
                else: self._agregar(n.der,d)
        def preorden(self,n,r=None):
            if r is None: r=[]
            if n is None: return r
            r.append(n.valor)
            self.preorden(n.izq,r); self.preorden(n.der,r)
            return r
        def inorden(self,n,r=None):
            if r is None: r=[]
            if n is None: return r
            self.inorden(n.izq,r); r.append(n.valor); self.inorden(n.der,r)
            return r
        def postorden(self,n,r=None):
            if r is None: r=[]
            if n is None: return r
            self.postorden(n.izq,r); self.postorden(n.der,r); r.append(n.valor)
            return r
        def to_dict(self,n):
            if n is None: return None
            return {"valor":n.valor,"izq":self.to_dict(n.izq),"der":self.to_dict(n.der)}

    arbol=Arbol()
    for d in datos: arbol.agregar(d)
    return {
        "datos":datos,
        "preorden":arbol.preorden(arbol.raiz),
        "inorden":arbol.inorden(arbol.raiz),
        "postorden":arbol.postorden(arbol.raiz),
        "arbol":arbol.to_dict(arbol.raiz)
    }

def run_abb_diccionario(secuencia=None):
    secuencia = secuencia or [1,13,11,5,9,10,1,12,3,6]

    class Nodo:
        def __init__(self,c): self.c=c; self.izq=None; self.der=None; self.pad=None

    vistos={}; indice={}; raiz=None

    def insertar(nodo,clave):
        if nodo is None:
            n=Nodo(clave); indice[clave]=n; return n
        if clave<nodo.c:
            nodo.izq=insertar(nodo.izq,clave)
            if nodo.izq: nodo.izq.pad=nodo
        elif clave>nodo.c:
            nodo.der=insertar(nodo.der,clave)
            if nodo.der: nodo.der.pad=nodo
        return nodo

    for num in secuencia:
        if num in vistos: continue
        vistos[num]=True; raiz=insertar(raiz,num)

    dic={}
    for clave,nodo in indice.items():
        dic[clave]=(nodo.izq.c if nodo.izq else None, nodo.der.c if nodo.der else None)

    return {"secuencia":secuencia,"diccionario":dic}

def run_grafos_bfs(start='A', grafo=None):
    from collections import deque
    grafo = grafo or {'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}
    visitado=set([start]); queue=deque([start]); lista=[]; pasos=[]
    pasos.append({"queue":list(queue),"visitados":list(visitado),"lista":[]})
    while queue:
        node=queue.popleft(); lista.append(node)
        for nx in grafo[node]:
            if nx not in visitado:
                visitado.add(nx); queue.append(nx)
        pasos.append({"procesado":node,"queue":list(queue),"visitados":list(visitado),"lista":list(lista)})
    return {"grafo":grafo,"start":start,"orden_bfs":lista,"pasos":pasos}

def run_dijkstra(inicio=0, destino=7, grafo=None):
    grafo = grafo or {
        0:[(1,9),(4,6)],1:[(0,9),(3,8)],2:[(5,6),(4,5)],
        3:[(1,8),(5,1),(7,7)],4:[(0,6),(2,5),(6,3)],
        5:[(3,1),(2,6)],6:[(4,3),(7,2)],7:[(3,7),(6,2)]
    }
    dist={n:float("inf") for n in grafo}; dist[inicio]=0
    prev={n:None for n in grafo}; pq=[(0,inicio)]
    pasos=[]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in grafo[u]:
            nd=d+w
            if nd<dist[v]:
                dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd,v))
        pasos.append({"nodo":u,"dist_actual":d,"distancias":{k:(v if v!=float("inf") else "∞") for k,v in dist.items()}})
    camino=[]; n=destino
    while n is not None: camino.append(n); n=prev[n]
    camino.reverse()
    return {
        "inicio":inicio,"destino":destino,
        "distancias":{k:(v if v!=float("inf") else "∞") for k,v in dist.items()},
        "camino":camino,"costo":dist[destino],"pasos":pasos
    }

# ====== PRACTICA 7: PRIM ======

def run_prim(start=2, grafo=None):
    grafo = grafo or {
        0:[(2,20),(1,10)],1:[(0,10),(3,50),(4,10)],
        2:[(0,20),(3,20),(4,33)],3:[(1,50),(2,20),(4,20),(5,2)],
        4:[(1,10),(2,33),(3,20),(5,1)],5:[(4,1),(3,2)]
    }
    visited=[False]*len(grafo); visited[start]=True
    mst=[]; total=0
    for _ in range(len(grafo)-1):
        min_w=float('inf'); u=-1; v=-1
        for i in range(len(grafo)):
            if visited[i]:
                for nb,w in grafo[i]:
                    if not visited[nb] and w<min_w:
                        min_w=w; u=i; v=nb
        visited[v]=True; mst.append({"de":u,"a":v,"costo":min_w}); total+=min_w
    return {"mst":mst,"total":total,"start":start,"nodos":len(grafo)}

# ====== ORDENAMIENTO ======

def run_sorts(lista=None):
    base = lista or [10,50,23,3,43,23,29,49,12,40]
    resultados={}

    def bubble(l):
        l=list(l); n=len(l)
        for i in range(n):
            for j in range(n-i-1):
                if l[j]>l[j+1]: l[j],l[j+1]=l[j+1],l[j]
        return l
    resultados["Bubble Sort"]=bubble(base)

    def selection(l):
        l=list(l); n=len(l)
        for i in range(n):
            mi=i
            for j in range(i+1,n):
                if l[j]<l[mi]: mi=j
            l[i],l[mi]=l[mi],l[i]
        return l
    resultados["Selection Sort"]=selection(base)

    def insertion(l):
        l=list(l)
        for i in range(1,len(l)):
            key=l[i]; j=i-1
            while j>=0 and key<l[j]: l[j+1]=l[j]; j-=1
            l[j+1]=key
        return l
    resultados["Insertion Sort"]=insertion(base)

    def merge(l):
        l=list(l)
        def ms(a):
            if len(a)<=1: return a
            m=len(a)//2; L=ms(a[:m]); R=ms(a[m:])
            r=[]; i=j=0
            while i<len(L) and j<len(R):
                if L[i]<R[j]: r.append(L[i]); i+=1
                else: r.append(R[j]); j+=1
            return r+L[i:]+R[j:]
        return ms(l)
    resultados["Merge Sort"]=merge(base)

    def quick(l):
        l=list(l)
        def qs(a):
            if len(a)<=1: return a
            p=a[len(a)//2]
            return qs([x for x in a if x<p])+[x for x in a if x==p]+qs([x for x in a if x>p])
        return qs(l)
    resultados["Quick Sort"]=quick(base)

    def counting(l):
        if not l: return []
        mx=max(l); cnt=[0]*(mx+1)
        for n in l: cnt[n]+=1
        r=[]
        for i,c in enumerate(cnt): r.extend([i]*c)
        return r
    resultados["Counting Sort"]=counting(base)

    return {"lista_original":base,"resultados":resultados}
