class ArbolABB:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.izquierdo = None
            self.derecho = None

    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = self.Nodo(dato)
        else:
            self.__agregar_recursivo(self.raiz, dato)

    # principal 
    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = self.Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = self.Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecho, dato)

    # PREORDEN: raiz - izquierda - derecha
    def preorden(self, nodo):
        if nodo is None:
            return

        print(nodo.valor, end=" ")

        # imprimir none si falta izquierdo pero existe derecho
        if nodo.izquierdo is None and nodo.derecho is not None:
            print("None", end=" ")

        # imprimir none si falta derecho pero existe izquierdo
        if nodo.derecho is None and nodo.izquierdo is not None:
            print("None", end=" ")

        self.preorden(nodo.izquierdo)
        self.preorden(nodo.derecho)

    # INORDEN: izquierda - raiz - derecha
    def inorden(self, nodo):
        if nodo is None:
            return

        # si falta izquierdo pero hay derecho, imprimir none antes
        if nodo.izquierdo is None and nodo.derecho is not None:
            print("None", end=" ")

        self.inorden(nodo.izquierdo)
        print(nodo.valor, end=" ")
        self.inorden(nodo.derecho)

        # si falta derecho pero hay izquierdo, imprimir none despues
        if nodo.derecho is None and nodo.izquierdo is not None:
            print("None", end=" ")

    # POSTORDEN: izquierda - derecha - raiz
    def postorden(self, nodo):
        if nodo is None:
            return

        # si falta izquierdo pero hay derecho, imprimir none antes
        if nodo.izquierdo is None and nodo.derecho is not None:
            print("None", end=" ")

        self.postorden(nodo.izquierdo)
        self.postorden(nodo.derecho)

        # si falta derecho pero hay izquierdo, imprimir none despues
        if nodo.derecho is None and nodo.izquierdo is not None:
            print("None", end=" ")

        print(nodo.valor, end=" ")


# --- EJEMPLO ---
arbol = ArbolABB()
datos = [3, 1, 4, 2, 5]

for d in datos:
    arbol.agregar(d)

print("Preorden:", end=" ")
arbol.preorden(arbol.raiz)

print("\nInorden:", end=" ")
arbol.inorden(arbol.raiz)

print("\nPostorden:", end=" ")
arbol.postorden(arbol.raiz)