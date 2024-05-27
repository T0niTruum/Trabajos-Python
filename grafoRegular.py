import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import networkx as nx

def ventanaRegular(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("Grafo Regular")
    ventana.geometry("500x200")
    texto = "Un grafo Regular es aquel que todos los grados de sus nodos o vertices son iguales"
    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    button_dibujar = tk.Button(ventana, foreground="#80DAEB", text="Verificar Grafo Regular", command=grafoRegular, fg="black")
    button_dibujar.pack()
    ventana.mainloop()

    return ventana

def grafoRegular():
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

    grafoRegular = es_Regular(G)
    if grafoRegular:
        messagebox.showinfo("Resultado", "El grafo es regular.")
    else:
        messagebox.showinfo("Resultado", "El grafo no es regular, sus nodos son de grado diferente.")
    # Dibujar el grafo
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, edge_color='k', linewidths=1, font_size=15)

    # Mostrar el grafo
    plt.title("Grafo")
    plt.show()

def es_Regular(G):
    grados = [G.degree(nodo) for nodo in G.nodes()]
    return all(grado == grados[0] for grado in grados)
