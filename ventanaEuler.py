import tkinter as tk

import matplotlib.pyplot as plt
import networkx as nx

from euleriano import dibujar_grafo, es_euleriano
from introGrafoEuler import ventanas_grafos_eulerianos


def crear_ventana_euler():
    windwos = tk.Tk()
    windwos.geometry("200x200")
    label_titulo = tk.Label(windwos, text="Introcudción grafos y ciclos eulerianos")
    label_titulo.pack()
    button_introducion_ciclos_eulerrianos = tk.Button(
        windwos,
        text="Introducción a los ciclos eulerianos",
        command=ventanas_grafos_eulerianos,
    )
    button_introducion_ciclos_eulerrianos.pack()
    button_introducion_ciclos_eulerrianos.place()

    button_grafo_eulerinao = tk.Button(
        windwos, text="Grafo euleriano", command=dibujar_grafo
    )
    button_grafo_eulerinao.pack()
    button_grafo_eulerinao.place()
    return windwos