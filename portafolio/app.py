from flask import Flask, render_template, jsonify, request
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from ejercicios.practica1 import *
from ejercicios.practica2 import *
from ejercicios.practica3_4 import *
from ejercicios.practica5_6_7 import *

app = Flask(__name__)

EJERCICIOS = [
    # Práctica 1
    {"id":"calificaciones","nombre":"Calificaciones","practica":"Práctica 1","tema":"Listas","descripcion":"Promedio, aprobados, reprobados y estadísticas de calificaciones usando arreglos.","icono":"chart-bar","color":"teal"},
    {"id":"cosechas","nombre":"Cosechas","practica":"Práctica 1","tema":"Listas","descripcion":"Análisis de cosechas anuales: promedio y clasificación por encima/debajo del promedio.","icono":"plant","color":"green"},
    {"id":"numrepetidos","nombre":"Números Repetidos","practica":"Práctica 1","tema":"Listas","descripcion":"Detección de duplicados y eliminación de repetidos sin usar sets.","icono":"list-numbers","color":"blue"},
    {"id":"palabras","nombre":"Frecuencia de Letras","practica":"Práctica 1","tema":"Listas","descripcion":"Conteo de letras únicas con clasificación mayúscula/minúscula usando arreglos.","icono":"abc","color":"purple"},
    {"id":"palabrasnoarr","nombre":"Letras Sin Arreglos","practica":"Práctica 1","tema":"Listas","descripcion":"Mismo problema que palabras pero sin usar arreglos — solo variables individuales.","icono":"variable","color":"coral"},
    # Práctica 2
    {"id":"coordenadas","nombre":"Coordenadas en Matriz","practica":"Práctica 2","tema":"Matrices","descripcion":"Busca todas las posiciones de un valor en una matriz 6×6.","icono":"grid-dots","color":"blue"},
    {"id":"matrices","nombre":"Multiplicación de Matrices","practica":"Práctica 2","tema":"Matrices","descripcion":"Multiplicación de matrices 3×3 de dos formas: triple for y comprensión de listas.","icono":"math-function","color":"amber"},
    {"id":"matrizbooleana","nombre":"Reserva de Asientos","practica":"Práctica 2","tema":"Matrices Booleanas","descripcion":"Sistema de reservas de asientos usando matriz booleana. Soporta RESERVAR, LIBERAR, CONSULTAR.","icono":"armchair","color":"teal"},
    {"id":"dataframe","nombre":"Estadísticas Housing","practica":"Práctica 2","tema":"DataFrames","descripcion":"Cálculo manual de media, moda, varianza y desviación estándar sobre datos de casas reales.","icono":"table","color":"green"},
    # Práctica 3
    {"id":"colas","nombre":"Cola Básica","practica":"Práctica 3","tema":"Colas","descripcion":"Implementación de cola con enqueue, dequeue, peek, is_empty y size usando listas.","icono":"stack-2","color":"orange"},
    {"id":"fila_banco","nombre":"Fila de Banco","practica":"Práctica 3","tema":"Colas","descripcion":"Simulación de fila bancaria con múltiples cuentas, retiros y depósitos.","icono":"building-bank","color":"blue"},
    {"id":"bicolas","nombre":"BiCola","practica":"Práctica 3","tema":"Colas","descripcion":"Bicola circular con enqueue al frente y al final, historial de retiros bancarios.","icono":"arrows-left-right","color":"purple"},
    # Práctica 4
    {"id":"cola_circular","nombre":"Cola Circular","practica":"Práctica 4","tema":"Colas Avanzadas","descripcion":"Cola circular con arreglo de capacidad fija. Visualiza el estado del arreglo interno.","icono":"circle-dotted","color":"coral"},
    {"id":"limitador","nombre":"Limitador de Peticiones","practica":"Práctica 4","tema":"Colas Avanzadas","descripcion":"Rate limiter usando deque con maxlen. Simula llegada de peticiones con ventana de tiempo.","icono":"clock","color":"amber"},
    {"id":"registro","nombre":"Registro de Intentos","practica":"Práctica 4","tema":"Colas Avanzadas","descripcion":"Cola de tareas con reintentos: las fallidas van al final, las exitosas al frente.","icono":"refresh","color":"green"},
    # Práctica 5
    {"id":"pilas","nombre":"Ordenamiento con Pila","practica":"Práctica 5","tema":"Pilas","descripcion":"Ordena una lista de precios usando una Pila y una Cola como estructuras auxiliares.","icono":"layers","color":"teal"},
    # Práctica 6
    {"id":"ejemplo_arbol","nombre":"Árbol Binario de Búsqueda","practica":"Práctica 6","tema":"Árboles","descripcion":"ABB con inserción y recorridos: preorden, inorden y postorden.","icono":"binary-tree","color":"green"},
    {"id":"abb_diccionario","nombre":"ABB → Diccionario","practica":"Práctica 6","tema":"Árboles","descripcion":"Construye un ABB y lo convierte a diccionario mostrando hijos izquierdo y derecho de cada nodo.","icono":"book","color":"blue"},
    {"id":"grafos_bfs","nombre":"BFS en Grafos","practica":"Práctica 6","tema":"Grafos","descripcion":"Búsqueda por amplitud (BFS) en un grafo no dirigido, paso a paso.","icono":"topology-star","color":"purple"},
    {"id":"dijkstra","nombre":"Algoritmo de Dijkstra","practica":"Práctica 6","tema":"Grafos","descripcion":"Ruta más corta entre nodos usando cola de prioridad (heap). Muestra distancias y camino.","icono":"route","color":"coral"},
    # Práctica 7
    {"id":"prim","nombre":"Algoritmo de Prim","practica":"Práctica 7","tema":"Grafos","descripcion":"Árbol de expansión mínima usando Prim. Muestra aristas elegidas y costo total.","icono":"git-branch","color":"amber"},
    # Ordenamiento
    {"id":"sorts","nombre":"Algoritmos de Ordenamiento","practica":"Ordenamiento","tema":"Sorts","descripcion":"7 algoritmos: Bubble, Selection, Insertion, Merge, Quick, Random Quick y Counting Sort.","icono":"arrow-up-down","color":"teal"},
]

@app.route('/')
def index():
    practicas = {}
    for e in EJERCICIOS:
        p = e['practica']
        if p not in practicas: practicas[p] = []
        practicas[p].append(e)
    return render_template('index.html', ejercicios=EJERCICIOS, practicas=practicas)

@app.route('/ejercicio/<eid>')
def ejercicio(eid):
    ej = next((e for e in EJERCICIOS if e['id']==eid), None)
    if not ej: return "No encontrado", 404
    return render_template('ejercicio.html', ej=ej, ejercicios=EJERCICIOS)

@app.route('/api/run/<eid>', methods=['POST'])
def run_ejercicio(eid):
    data = request.get_json(silent=True) or {}
    try:
        if eid == 'calificaciones':
            inp = data.get('calificaciones')
            if inp:
                inp = [float(x) for x in str(inp).split(',')]
            result = run_calificaciones(inp)
        elif eid == 'cosechas':
            inp = data.get('cosechas')
            if inp:
                inp = [float(x) for x in str(inp).split(',')]
            result = run_cosechas(inp)
        elif eid == 'numrepetidos':
            inp = data.get('numeros')
            if inp:
                inp = [int(x) for x in str(inp).split(',')]
            result = run_numrepetidos(inp)
        elif eid == 'palabras':
            result = run_palabras(data.get('palabra'))
        elif eid == 'palabrasnoarr':
            result = run_palabrasnoarr(data.get('palabra'))
        elif eid == 'coordenadas':
            v = int(data.get('valor', 7))
            result = run_coordenadas(v)
        elif eid == 'matrices':
            result = run_matrices()
        elif eid == 'matrizbooleana':
            result = run_matriz_booleana()
        elif eid == 'dataframe':
            path = os.path.join(os.path.dirname(__file__), 'data/Housing.csv')
            result = run_dataframe(path)
        elif eid == 'colas':
            result = run_colas()
        elif eid == 'fila_banco':
            result = run_fila_banco(
                int(data.get('cuentas',5)),
                int(data.get('retiro',500)),
                int(data.get('deposito',300))
            )
        elif eid == 'bicolas':
            result = run_bicolas()
        elif eid == 'cola_circular':
            cap = int(data.get('capacidad', 5))
            result = run_cola_circular(cap)
        elif eid == 'limitador':
            result = run_limitador()
        elif eid == 'registro':
            result = run_registro_intentos()
        elif eid == 'pilas':
            result = run_pilas()
        elif eid == 'ejemplo_arbol':
            inp = data.get('datos')
            if inp:
                inp = [int(x) for x in str(inp).split(',')]
            result = run_ejemplo_arbol(inp)
        elif eid == 'abb_diccionario':
            inp = data.get('secuencia')
            if inp:
                inp = [int(x) for x in str(inp).split(',')]
            result = run_abb_diccionario(inp)
        elif eid == 'grafos_bfs':
            result = run_grafos_bfs()
        elif eid == 'dijkstra':
            inicio = int(data.get('inicio', 0))
            destino = int(data.get('destino', 7))
            result = run_dijkstra(inicio, destino)
        elif eid == 'prim':
            result = run_prim()
        elif eid == 'sorts':
            inp = data.get('lista')
            if inp:
                inp = [int(x) for x in str(inp).split(',')]
            result = run_sorts(inp)
        else:
            return jsonify({"error": "Ejercicio no encontrado"}), 404
        return jsonify({"ok": True, "resultado": result})
    except Exception as ex:
        return jsonify({"ok": False, "error": str(ex)}), 500

@app.route('/viz/sorts')
def viz_sorts(): return render_template('viz_sorts.html', ejercicios=EJERCICIOS)

@app.route('/viz/arbol')
def viz_arbol(): return render_template('viz_arbol.html', ejercicios=EJERCICIOS)

@app.route('/viz/grafos')
def viz_grafos(): return render_template('viz_grafos.html', ejercicios=EJERCICIOS)

@app.route('/viz/colas')
def viz_colas(): return render_template('viz_colas.html', ejercicios=EJERCICIOS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
