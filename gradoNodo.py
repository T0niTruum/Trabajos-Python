import tkinter as tk
from tkinter import messagebox, simpledialog

import matplotlib.pyplot as plt
import networkx as nx

from conectividad import conectividad


def calcular_conectividad_nodo(G, nodo):
    conectividad_nodo = conectividad(G, nodo)
    print(f"Los nodos conectados al nodo {nodo} son: {conectividad_nodo}")


def definicion_grado_nodo():
    grado_no_dirigido = "El grado de un nodo en un grafo no dirigido son la cantidad de arcos (aristas ) que inciden en el nodo,en caso de que halla un loop, el arco se cuenta como entrada y salida\n"
    grafo_dirigido = "En un grafo dirigido el grado del nodo son aquellos arcos que inciden en el y los que salen de el\n "
    root = tk.Tk()

    texto = tk.Label(
        root,
        text=grado_no_dirigido + grafo_dirigido,
    )
    texto.pack()

    return


def obtener_grado_nodo(G, nodo):
    # Verificar si el nodo existe en el grafo
    if nodo in G:
        if nx.is_directed(G):
            grado_entrada = G.in_degree[nodo]
            grado_salida = G.out_degree[nodo]
            messagebox.showinfo("Grado del nodo", 
                f"El grado de entrada del nodo {nodo} es: {grado_entrada}\n"
                f"El grado de salida del nodo {nodo} es: {grado_salida}\n"
                f"Los nodos conectados al nodo son: {conectividad(G, nodo)}")
        else:
            grado = G.degree[nodo]
            messagebox.showinfo("Grado del nodo", 
                f"El grado del nodo {nodo} es: {grado}\n"
                f"Los nodos conectados al nodo son: {conectividad(G, nodo)}")
    else:
        messagebox.showerror("Error", f"El nodo {nodo} no existe en el grafo.")


def dibujar_grafo(ventana):
    # definicion_grado_nodo()
    # Crear un grafo vacío (dirigido o no dirigido)
    es_dirigido = simpledialog.askstring(
        "Tipo de grafo", "¿Quieres un grafo dirigido? (s/n): "
    )
    if es_dirigido is not None:
        es_dirigido = es_dirigido.lower() == "s"
    else:
        # Si el usuario no ingresa ninguna respuesta, asumimos un valor predeterminado (False)
        es_dirigido = False
    G = nx.DiGraph() if es_dirigido else nx.Graph()

    # Agregar nodos
    num_nodos = simpledialog.askinteger(
        "Número de nodos", "Ingresa el número de nodos:"
    )
    if num_nodos is None:  # Si se cancela el diálogo, salir de la función
        return

    for i in range(num_nodos):
        G.add_node(i)

    # Agregar aristas (enlaces)
    while True:
        u = simpledialog.askinteger(
            "Arista", f"Ingresa el nodo de origen (0-{num_nodos - 1}):"
        )
        v = simpledialog.askinteger(
            "Arista", f"Ingresa el nodo de destino (0-{num_nodos - 1}):"
        )
        if u is None or v is None:  # Si se cancela el diálogo, salir del bucle
            break
        G.add_edge(u, v)

        continuar = simpledialog.askstring(
            "Agregar otra arista", "¿Agregar otra arista? (s/n):"
        )
        if (
            continuar is None or continuar.lower() != "s"
        ):  # Si se cancela el diálogo o el usuario ingresa algo que no es "s", salir del bucle
            break

    # Obtener el grado de un nodo
    nodo_a_consultar = simpledialog.askinteger(
        "Grado de un nodo", "Ingresa el nodo a consultar:"
    )
    obtener_grado_nodo(G, nodo_a_consultar)

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
    plt.show()