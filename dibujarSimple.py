import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import networkx as nx


def comprobarSimple(grafo):
     # Verifica si hay bucles en el grafo
    tiene_bucles = any(grafo.has_edge(nodo, nodo) for nodo in grafo.nodes)

    # Verifica si hay múltiples aristas entre los mismos nodos
    tiene_multiples_aristas = any(grafo.has_edge(u, v) and grafo.has_edge(v, u) for u, v in grafo.edges)

    # El grafo es simple si no tiene bucles ni múltiples aristas
    return not tiene_bucles and not tiene_multiples_aristas

def dibujar_Simple():
    # Crear una ventana
    ventana = tk.Tk()
    ventana.title("Dibujo de Grafo y Verificación de Simplicidad")
    ventana.geometry("200x200")

    # Crear un frame para contener el grafo y el resultado de la verificación
    frame = tk.Frame(ventana)
    frame.pack(expand=True, fill="both")

    # Crear una figura para dibujar el grafo
    fig, ax = plt.subplots(figsize=(5, 5))

    es_dirigido = messagebox.askyesno("Tipo de grafo", "¿Quieres un grafo dirigido? (s/n):")
    G = nx.DiGraph() if es_dirigido else nx.Graph()

    # Agregar nodos
    num_nodos = simpledialog.askinteger("Nodos", "Ingresa el número de nodos:")
    if num_nodos is None:
        ventana.destroy()
        return
    
    G.add_nodes_from(range(num_nodos))

    # Agregar aristas (enlaces)
    while True:
        u = simpledialog.askinteger("Aristas", f"Ingresa el nodo de origen (0-{num_nodos - 1}):")
        v = simpledialog.askinteger("Aristas", f"Ingresa el nodo de destino (0-{num_nodos - 1}):")
        
        if u is None or v is None:
            break
        
        G.add_edge(u, v)
        
        continuar = messagebox.askyesno("Arista", "¿Quieres otra arista? (s/n):")
        if not continuar:
            break

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=500, node_color="skyblue", font_size=10)

    # Verificar si el grafo es simple y mostrar el resultado
    resultado = "El grafo es Simple" if comprobarSimple(G) else "El grafo no es Simple"
    resultado_label = tk.Label(ventana, text=resultado, font=("Arial", 12))
    resultado_label.pack(pady=10)

    plt.show()

    ventana.mainloop()