class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1

    def esta_vacia(self):
        return self.frente == -1

    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente

    def encolar(self, turno):
        if self.esta_llena():
            print("La cola esta llena")
            return

        if self.esta_vacia():
            self.frente = 0
            self.final = 0
        else:
            self.final = (self.final + 1) % self.capacidad

        self.cola[self.final] = turno

    def desencolar(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return None

        turno = self.cola[self.frente]
        self.cola[self.frente] = None

        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        else:
            self.frente = (self.frente + 1) % self.capacidad

        return turno

    def ver_frente(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return None
        return self.cola[self.frente]

    def mostrar(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return

        i = self.frente
        elementos = []

        while True:
            elementos.append(self.cola[i])
            if i == self.final:
                break
            i = (i + 1) % self.capacidad

        print("Cola:", elementos)

    def estado(self):
        print("Arreglo:", self.cola)
        print("Frente:", self.frente, "Final:", self.final)
        if self.esta_llena():
            print("La cola está llena. No se puede encolar.")
            return
        
        if self.esta_vacia():
            self.frente = 0
            self.final = 0
        else:
            self.final = (self.final + 1) % self.capacidad

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía. No se puede desencolar.")
            return None
        
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None  # Limpiar el espacio

        if self.frente == self.final:  # Solo había un elemento
            self.frente = -1
            self.final = -1
        else:
            self.frente = (self.frente + 1) % self.capacidad

        return elemento
    
    def ver_frente(self):
        if self.esta_vacia():
            print("La cola está vacía.")
            return None
        return self.cola[self.frente]
    
    def mostrar(self):
        if self.esta_vacia():
            print("La cola está vacía.")
            return
        
        elementos = []
        i = self.frente
        while True:
            elementos.append(self.cola[i])
            if i == self.final:
                break
            i = (i + 1) % self.capacidad
        
        print("Cola:", elementos)

#// Prueba de la ColaCircular

cola = ColaCircular(5)

# Insertar turnos
cola.encolar("T1")
cola.encolar("T2")
cola.encolar("T3")
cola.encolar("T4")
cola.encolar("T5")

cola.mostrar()
cola.estado()

# Atender turnos
print("Atendiendo:", cola.desencolar())
print("Atendiendo:", cola.desencolar())

cola.mostrar()
cola.estado()

# Insertar 
cola.encolar("T6")
cola.encolar("T7")

cola.mostrar()
cola.estado()

# Ver frente
print("Turno al frente:", cola.ver_frente())