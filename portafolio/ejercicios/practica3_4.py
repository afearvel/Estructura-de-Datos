from collections import deque

def run_colas():
    log = []
    lista = []
    def enque(e): lista.append(e)
    def deq(): return lista.pop(0) if lista else None
    def peek(): return lista[0] if lista else None

    log.append({"accion":"is_empty","resultado":lista==[],"lista":list(lista)})
    enque(1); log.append({"accion":"enqueue(1)","resultado":1,"lista":list(lista)})
    log.append({"accion":"is_empty","resultado":lista==[],"lista":list(lista)})
    deq(); log.append({"accion":"dequeue","resultado":"removido","lista":list(lista)})
    log.append({"accion":"is_empty","resultado":lista==[],"lista":list(lista)})
    enque(2); enque(3)
    log.append({"accion":"enqueue(2),enqueue(3)","resultado":"ok","lista":list(lista)})
    log.append({"accion":"peek","resultado":peek(),"lista":list(lista)})
    log.append({"accion":"size","resultado":len(lista),"lista":list(lista)})
    return {"pasos": log}

def run_fila_banco(n_cuentas=5, monto_retiro=500, monto_deposito=300):
    saldo = [1000]*n_cuentas
    retiros = []; depositos = []
    log = []
    for i in range(len(saldo)):
        s = saldo.pop(0)
        if s >= monto_retiro:
            s -= monto_retiro
            retiros.append(monto_retiro)
            log.append({"op":"retiro","monto":monto_retiro,"saldo":s,"ok":True})
        else:
            log.append({"op":"retiro","monto":monto_retiro,"saldo":s,"ok":False})
        saldo.append(s)
    for i in range(len(saldo)):
        s = saldo.pop(0)
        s += monto_deposito
        depositos.append(monto_deposito)
        log.append({"op":"deposito","monto":monto_deposito,"saldo":s,"ok":True})
        saldo.append(s)
    return {"saldos_finales":saldo,"retiros":retiros,"depositos":depositos,"log":log}

def run_bicolas():
    class BiCola:
        def __init__(self,cap):
            self.cap=cap; self.datos=[None]*cap
            self.head=0; self.tail=0; self.cnt=0
        def full(self): return self.cnt==self.cap
        def empty(self): return self.cnt==0
        def enqueue_final(self,e):
            if self.full(): return
            self.datos[self.tail]=e
            self.tail=(self.tail+1)%self.cap; self.cnt+=1
        def enqueue_frente(self,e):
            if self.full(): return
            self.head=(self.head-1)%self.cap
            self.datos[self.head]=e; self.cnt+=1
        def dequeue_frente(self):
            if self.empty(): return None
            e=self.datos[self.head]
            self.head=(self.head+1)%self.cap; self.cnt-=1; return e
        def peek_frente(self):
            return self.datos[self.head] if not self.empty() else None
        def mostrar(self):
            r=[]; i=self.head
            for _ in range(self.cnt):
                r.append(self.datos[i]); i=(i+1)%self.cap
            return r

    saldos=BiCola(10); historial=BiCola(20)
    for _ in range(5): saldos.enqueue_final(1000)
    retiros=[500,400,300,200,100]
    for m in retiros:
        s=saldos.dequeue_frente()
        historial.enqueue_frente(f"-{m}")
        saldos.enqueue_final(s-m)
    return {
        "historial":historial.mostrar(),
        "saldos_finales":saldos.mostrar(),
        "saldo_frente":saldos.peek_frente(),
        "tam_historial":historial.cnt
    }

def run_cola_circular(capacidad=5, turnos=None):
    turnos = turnos or ["T1","T2","T3","T4","T5"]
    class ColaCircular:
        def __init__(self,cap):
            self.cap=cap; self.cola=[None]*cap
            self.frente=-1; self.final=-1
        def vacia(self): return self.frente==-1
        def llena(self): return (self.final+1)%self.cap==self.frente
        def encolar(self,t):
            if self.llena(): return False
            if self.vacia(): self.frente=0; self.final=0
            else: self.final=(self.final+1)%self.cap
            self.cola[self.final]=t; return True
        def desencolar(self):
            if self.vacia(): return None
            t=self.cola[self.frente]; self.cola[self.frente]=None
            if self.frente==self.final: self.frente=-1; self.final=-1
            else: self.frente=(self.frente+1)%self.cap
            return t
        def ver_frente(self): return self.cola[self.frente] if not self.vacia() else None
        def mostrar(self):
            if self.vacia(): return []
            r=[]; i=self.frente
            while True:
                r.append(self.cola[i])
                if i==self.final: break
                i=(i+1)%self.cap
            return r
        def estado(self): return list(self.cola)

    cc=ColaCircular(capacidad)
    log=[]
    for t in turnos: cc.encolar(t)
    log.append({"momento":"inicial","cola":cc.mostrar(),"array":cc.estado()})
    a1=cc.desencolar(); a2=cc.desencolar()
    log.append({"momento":"después de 2 atenciones","atendidos":[a1,a2],"cola":cc.mostrar(),"array":cc.estado()})
    cc.encolar("T6"); cc.encolar("T7")
    log.append({"momento":"después de encolar T6,T7","cola":cc.mostrar(),"array":cc.estado()})
    return {"log":log,"frente":cc.ver_frente(),"capacidad":capacidad}

def run_limitador(limite=10, tiempos=None):
    tiempos = tiempos or [0,2,4,6,12]
    cola=deque(maxlen=3); log=[]
    for x in tiempos:
        accion={}; accion["tiempo"]=x
        if cola and x-cola[0]>=limite:
            vaciados=list(cola); cola.clear()
            accion["evento"]="reset por tiempo"; accion["vaciados"]=vaciados
        elif len(cola)==cola.maxlen:
            old=cola.popleft()
            accion["evento"]="dequeue por capacidad"; accion["removido"]=old
        else:
            accion["evento"]="enqueue normal"
        cola.append(x); accion["cola"]=list(cola)
        log.append(accion)
    return {"log":log,"limite":limite}

def run_registro_intentos(tareas=None):
    tareas = tareas or [["T1",1,0],["T2",0,0],["T3",2,0],["T4",1,0],["T5",2,2],["T6",2,1]]
    cola=deque([list(t) for t in tareas])
    log=[{"momento":"inicial","cola":[x[0] for x in cola]}]
    completadas=0; n=len(tareas)
    while completadas<n:
        tarea=cola.popleft()
        nombre,fallos,intentos=tarea[0],tarea[1],tarea[2]
        if fallos>0:
            tarea[1]-=1; tarea[2]+=1
            cola.append(tarea)
            log.append({"tarea":nombre,"resultado":"fallo","intentos":tarea[2],"cola":[x[0] for x in cola]})
        else:
            cola.appendleft(tarea); completadas+=1
            log.append({"tarea":nombre,"resultado":"éxito","intentos":intentos,"cola":[x[0] for x in cola]})
    return {"log":log}
