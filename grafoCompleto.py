import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import networkx as nx

def ventanaCompleto(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("Grafo Completo")
    ventana.geometry("500x250")
    texto = "un grafo completo es un grafo simple donde cada par de vértices está conectado por una arista. \nUn grafo completo de n vértices tiene 𝑛(𝑛−1)/2 aristas, y se denota 𝐾𝑛. \nEs un grafo regular con todos sus vértices de grado 𝑛−1."

    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    button_dibujar = tk.Button(ventana, foreground="#80DAEB", text="Dibujar grafo completo", command=grafoCompleto, fg="black")
    button_dibujar.pack()
    ventana.mainloop()

    return ventana

def grafoCompleto():
    num_nodos = simpledialog.askinteger("Número de nodos", "Ingresa el número de nodos:")
    if num_nodos is None:
        messagebox.showerror("Error", "Número de nodos no ingresado.")
        return

    G = nx.complete_graph(num_nodos)

    # Dibujar el grafo
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='k', linewidths=1, font_size=15)

    # Mostrar el grafo
    plt.title(f"Grafo Completo con {num_nodos} Nodos")
    plt.show()
