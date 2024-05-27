import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import networkx as nx

def ventanaCompleto(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("Grafo Completo")
    ventana.geometry("500x125")
    ventana.configure(bg="#d2f4e4")
    texto = "Un grafo completo es un grafo simple donde cada par de vértices está conectado por una arista."

    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, bg="#d2f4e4", text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    button_dibujar = tk.Button(ventana, foreground="white", background="#80DAEB", text="Dibujar grafo completo", command=grafoCompleto)
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
