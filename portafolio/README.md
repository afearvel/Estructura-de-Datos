# Portafolio — Estructuras de Datos

Aplicación web interactiva con todos los ejercicios del semestre.


## Instalación

```bash
pip install flask pandas
```

## Ejecutar

```bash
python app.py
```

Luego abre tu navegador en: **http://localhost:5000**

## Estructura del proyecto

```
portafolio/
├── app.py                    ← Servidor Flask (punto de entrada)
├── data/
│   └── Housing.csv           ← Dataset para Práctica 2
├── ejercicios/
│   ├── practica1.py          ← Listas (calificaciones, cosechas, etc.)
│   ├── practica2.py          ← Matrices y DataFrames
│   ├── practica3_4.py        ← Colas (simple, circular, bicola, etc.)
│   └── practica5_6_7.py      ← Pilas, Árboles, Grafos, Sorts
└── templates/
    ├── base.html             ← Layout con sidebar
    ├── index.html            ← Dashboard principal
    └── ejercicio.html        ← Página interactiva por ejercicio
```

## Ejercicios incluidos (22 en total)

| Práctica | Ejercicio | Tema |
|----------|-----------|------|
| Ordenamiento | Sorts | Bubble, Selection, Insertion, Merge, Quick, Counting |
| Práctica 1 | Calificaciones | Listas |
| Práctica 1 | Cosechas | Listas |
| Práctica 1 | Números Repetidos | Listas |
| Práctica 1 | Frecuencia de Letras | Listas |
| Práctica 1 | Letras Sin Arreglos | Listas |
| Práctica 2 | Coordenadas en Matriz | Matrices |
| Práctica 2 | Multiplicación de Matrices | Matrices |
| Práctica 2 | Reserva de Asientos | Matrices Booleanas |
| Práctica 2 | Estadísticas Housing | DataFrames |
| Práctica 3 | Cola Básica | Colas |
| Práctica 3 | Fila de Banco | Colas |
| Práctica 3 | BiCola | Colas |
| Práctica 4 | Cola Circular | Colas Avanzadas |
| Práctica 4 | Limitador de Peticiones | Colas Avanzadas |
| Práctica 4 | Registro de Intentos | Colas Avanzadas |
| Práctica 5 | Ordenamiento con Pila | Pilas |
| Práctica 6 | Árbol Binario de Búsqueda | Árboles |
| Práctica 6 | ABB → Diccionario | Árboles |
| Práctica 6 | BFS en Grafos | Grafos |
| Práctica 6 | Dijkstra | Grafos |
| Práctica 7 | Prim | Grafos |
