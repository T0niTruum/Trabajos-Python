from tkinter import messagebox, simpledialog

import matplotlib.pyplot as plt
import networkx as nx


def es_euleriano(G):
    if nx.is_directed(G):
        if nx.is_weakly_connected(G):
            messagebox.showinfo(
                "Resultado",
                "El grafo no es euleriano ni tiene camino euleriano porque es débilmente conexo."
            )
            return False
    else:
        if not nx.is_connected(G):
            messagebox.showinfo(
                "Resultado",
                "El grafo no es euleriano ni tiene camino euleriano porque no es conexo."
            )
            return False

    num_impares = sum(deg % 2 != 0 for _, deg in G.degree)
    if num_impares == 0:
        messagebox.showinfo("Resultado", "El grafo es euleriano.")
        return True
    elif num_impares == 2:
        messagebox.showinfo("Resultado", "El grafo tiene un camino euleriano.")
        return True
    else:
        messagebox.showinfo("Resultado", "El grafo no es euleriano ni tiene camino euleriano.")
        return False


def dibujar_grafo():
    # Crear un grafo vacío (dirigido o no dirigido)
    es_dirigido = messagebox.askyesno(
        "Tipo de grafo", "¿Quieres un grafo dirigido? (s/n):"
    )
    G = nx.DiGraph() if es_dirigido else nx.Graph()

    # Agregar nodos
    num_nodos = simpledialog.askinteger("Nodos", "¿Cuántos nodos quieres agregar?")
    if num_nodos is None:  # Si se cancela el diálogo, salir de la función
        return

    # Agregar aristas (enlaces)
    while True:
        u = simpledialog.askinteger(
            "Input", "Ingresa el nodo de origen (0-{0}): ".format(num_nodos - 1)
        )
        v = simpledialog.askinteger(
            "Input", "Ingresa el nodo de destino (0-{0}): ".format(num_nodos - 1)
        )
        G.add_edge(u, v)

        continuar = simpledialog.askstring("Input", "¿Agregar otra arista? (s/n): ")
        if continuar != "s":
            break

    # Opciones para el usuario
    opcion = simpledialog.askstring(
        "input",
        "¿Qué deseas verificar?\n1. Si es euleriano.\n2. Si tiene un camino euleriano.\nSelecciona una opción (1/2): ",
    )

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)

    if opcion == "1":
        es_euleriano(G)
    elif opcion == "2":
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color="r")
        es_euleriano(G)

    plt.show()


if __name__ == "__main__":
    dibujar_grafo()
