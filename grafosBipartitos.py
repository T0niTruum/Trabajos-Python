import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import networkx as nx

def ventanaBipartito(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("Grafo Bipartito")
    ventana.geometry("500x350")
    texto = ("Un grafo bipartito es un grafo cuyos vértices se pueden separar en dos conjuntos disjuntos, de manera que las aristas no pueden relacionar vértices de un mismo conjunto. \n"
            "Un grafo bipartito puede considerarse si todos los vértices de uno de los subconjuntos están relacionados con los del otro subconjunto.")

    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    button_dibujar = tk.Button(ventana, text="Generar grafo Bipartito", command=grafoBipartito, fg="black")
    button_dibujar.pack()
    button_dibujar.place(x=100, y=100)
    button_dibujarPropio=tk.Button(ventana, text="Dibujar grafo Bipartito", command=dibujarGrafoBipartito, fg="black")
    button_dibujarPropio.pack()
    button_dibujarPropio.place(x=100, y=200)
    ventana.mainloop()

    return ventana

def grafoBipartito():
    num_nodos_conjunto_1 = simpledialog.askinteger("Conjunto 1", "Ingresa el número de nodos para el conjunto 1:")
    if num_nodos_conjunto_1 is None:
        return

    num_nodos_conjunto_2 = simpledialog.askinteger("Conjunto 2", "Ingresa el número de nodos para el conjunto 2:")
    if num_nodos_conjunto_2 is None:
        return

    G = nx.Graph()

    # Crear los nodos para el conjunto 1
    nodos_conjunto_1 = [f"U{i}" for i in range(num_nodos_conjunto_1)]
    # Crear los nodos para el conjunto 2
    nodos_conjunto_2 = [f"V{i}" for i in range(num_nodos_conjunto_2)]

    # Agregar nodos al grafo
    G.add_nodes_from(nodos_conjunto_1, bipartite=0)
    G.add_nodes_from(nodos_conjunto_2, bipartite=1)

    # Agregar aristas entre cada nodo de conjunto 1 y cada nodo de conjunto 2
    for u in nodos_conjunto_1:
        for v in nodos_conjunto_2:
            G.add_edge(u, v)

    # Dibujar el grafo bipartito

    # Posiciones de los nodos para el grafo bipartito
    pos = {}
    pos.update((n, (1, i)) for i, n in enumerate(nodos_conjunto_1))  # Nodos en y=1
    pos.update((n, (2, i)) for i, n in enumerate(nodos_conjunto_2))  # Nodos en y=2

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='k', linewidths=1, font_size=15)
    plt.title("Grafo Bipartito")
    plt.show()


def dibujarGrafoBipartito():
    
    # Crear una ventana con dos subfiguras
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    #quitamos el grafico generado automaticamente
    ax2.axis("off")
    
    es_dirigido = messagebox.askyesno(
        "Tipo de grafo", "¿Quieres un grafo dirigido? (s/n):"
    )
    G = nx.DiGraph() if es_dirigido else nx.Graph()

    # Agregar nodos
    num_nodos = simpledialog.askinteger("Nodos","ingresa el numero de nodos:")
    if num_nodos is None:
        return
    
    for i in range(num_nodos):
        G.add_node(i)

    # Agregar aristas (enlaces)
    while True:
        u=simpledialog.askinteger("Aristas","Ingresa el nodo de origen (0-{0}): ".format(num_nodos - 1))
        v=simpledialog.askinteger("Aristas","Ingresa el nodo de destino (0-{0}): ".format(num_nodos - 1))
        
        G.add_edge(u, v)
        
        continuar = messagebox.askyesno(
        "Arista", "¿Quieres otra arista? (s/n):"
    )
        if not continuar:
            break

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    #creamos el grafo en ax1
    nx.draw(G, pos,ax=ax1,with_labels=True, node_size=500, node_color="skyblue", font_size=10)
    
    
    if comprobarBipartito(G):
        nx.draw_networkx_edges(G, pos,ax=ax1, width=2, alpha=0.5, edge_color="r")
        text="El grafo es Bipartito"
        ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
    else:
        nx.draw_networkx_edges(G, pos,ax=ax1, width=2, alpha=0.5, edge_color="r")
        text="El grafo no es Bipartito"
        ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
        
    plt.show()

def comprobarBipartito(G):
    n=len(G)
    visitado= [False]*n
    camino=[]

    def recorrer(node,nodeinicio):
        visitado[node]=True
        camino.append(node)
        
        for vecino in G[node]:
            if not visitado[vecino]:
                if recorrer(vecino,nodeinicio):
                    return True         
                           
        for v in range(n):
            if visitado[v] == False:
                if recorrer(v,v):
                    return True
                
        
        for vecino in G[node]:
            if vecino==nodeinicio:
                if len(camino)%2!=0:
                    return False
                else:
                    return True
                
    if recorrer(0,0):
        return True
    else:    
        return False