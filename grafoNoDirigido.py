import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import networkx as nx
import random

def ventanaNoDirigido(ventana):
    ventana = tk.Tk()
    ventana.title("Grafo No Dirigido")
    ventana.geometry("500x150")
    ventana.configure(bg="#d2f4e4")
    
    # Función para mostrar información sobre grafo no dirigido
    texto = "Tipo de grafo en el que sus aristas no constan de una dirección, permitiendo recorrer el grafo en cualquier dirección."
    label = tk.Label(ventana, bg="#d2f4e4",text=texto, wraplength=480)
    label.pack()

    # Botón para dibujar el grafo
    button_dibujar = tk.Button(ventana, background="#80DAEB", text="Dibujar grafo No Dirigido", command=dibujar_grafoNoDirigido, fg="white")
    button_dibujar.pack(pady=15)
    button_ejemplo =tk.Button(ventana, background="#80DAEB", text="Grafo de ejemplo", command=dibujar_grafoRandom, fg ="white")
    button_ejemplo.pack(pady=5)

    ventana.mainloop()

def dibujar_grafoNoDirigido():
    # Crear un grafo no dirigido
    g = nx.Graph()

    # Solicitar al usuario el número de nodos
    num_nodos=0
    num_nodos = simpledialog.askinteger("Número de Nodos", "Ingresa el número de nodos:")
    if num_nodos is None:  # Si se cancela el diálogo, salir de la función
        return
    
    for i in range(num_nodos):
        g.add_node(i)

    # Solicitar al usuario las aristas
    while True:
        u = simpledialog.askinteger("Arista", f"Ingresa el nodo de origen (0-{num_nodos - 1}):")
        v = simpledialog.askinteger("Arista", f"Ingresa el nodo de destino (0-{num_nodos - 1}):")
        if u is None or v is None:  # Si se cancela el diálogo, salir del bucle
            break
        g.add_edge(u, v)

        continuar = simpledialog.askstring("Agregar otra arista", "¿Agregar otra arista? (s/n):")
        if continuar is None or continuar.lower() != "s":  # Si se cancela el diálogo o el usuario ingresa algo que no es "s", salir del bucle
            break

    # Dibujar el grafo
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
    plt.show()

def dibujar_grafoRandom():
    # Generar un número aleatorio de nodos entre 5 y 15
    num_nodos = random.randint(1, 6)
    
    # Generar un número aleatorio de aristas entre 0 y num_nodos * (num_nodos - 1) / 2
    max_aristas = num_nodos * (num_nodos - 1) // 2
    num_aristas = random.randint(0, max_aristas)
    
    # Generar un grafo aleatorio con el número de nodos y aristas generados
    g = nx.gnm_random_graph(num_nodos, num_aristas)
    
    # Dibujar el grafo
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
    plt.show()