import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt

def ventanaAciclico(ventana):
    ventana = tk.Tk()
    ventana.title("Grafo Aciclico")
    ventana.geometry("500x200")
    
    # Función para mostrar información sobre grafo aciclico
    texto = "Un gráfico acíclico es un gráfico sin ciclos (un ciclo es un circuito completo). Al seguir el gráfico de nodo a nodo, nunca visitará el mismo nodo dos veces."
    label = tk.Label(ventana, text=texto, wraplength=480)
    label.pack()

    # Botón para dibujar el grafo
    button_dibujar = tk.Button(ventana, text="Verificar si un grafo es aciclico", command=verificar_grafoAciclico, fg="black")
    button_dibujar.pack()

    ventana.mainloop()

def verificar_grafoAciclico():
    es_dirigido = simpledialog.askstring("Tipo de grafo", "¿Quieres un grafo dirigido? (s/n): ")
    if es_dirigido is not None:
        es_dirigido = es_dirigido.lower() == "s"
    else:
        # Si el usuario no ingresa ninguna respuesta, asumimos un valor predeterminado (False)
        es_dirigido = False
    G = nx.DiGraph() if es_dirigido else nx.Graph()

    # Agregar nodos
    num_nodos = simpledialog.askinteger("Número de nodos", "Ingresa el número de nodos:")
    if num_nodos is None:  # Si se cancela el diálogo, salir de la función
        return
    
    for i in range(num_nodos):
        G.add_node(i)

    # Agregar aristas (enlaces)
    while True:
        u = simpledialog.askinteger("Arista", f"Ingresa el nodo de origen (0-{num_nodos - 1}):")
        v = simpledialog.askinteger("Arista", f"Ingresa el nodo de destino (0-{num_nodos - 1}):")
        if u is None or v is None:  # Si se cancela el diálogo, salir del bucle
            break
        G.add_edge(u, v)

        continuar = simpledialog.askstring("Agregar otra arista", "¿Agregar otra arista? (s/n):")
        if continuar is None or continuar.lower() != "s":  # Si se cancela el diálogo o el usuario ingresa algo que no es "s", salir del bucle
            break

    if es_dirigido:
        es_aciclico = nx.is_directed_acyclic_graph(G)
    else:
        es_aciclico = es_aciclico_no_dirigido(G)

    if es_aciclico:
        messagebox.showinfo("Resultado", "El grafo es acíclico (no tiene ciclos).")
    else:
        messagebox.showinfo("Resultado", "El grafo tiene ciclos, por lo tanto, no es acíclico.")
    # Dibujar el grafo
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='k', linewidths=1, font_size=15)

    # Mostrar el grafo
    plt.title("Grafo")
    plt.show()

    

def es_aciclico_util(G, v, visitados, padre):
    visitados[v] = True

    for vecino in G.neighbors(v):
        if not visitados[vecino]:
            if es_aciclico_util(G, vecino, visitados, v):
                return True
        elif vecino != padre:
            return True

    return False

def es_aciclico_no_dirigido(G):
    visitados = {nodo: False for nodo in G.nodes()}

    for nodo in G.nodes():
        if not visitados[nodo]:
            if es_aciclico_util(G, nodo, visitados, -1):
                return False
    return True