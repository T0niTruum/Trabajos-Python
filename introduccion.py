import tkinter as tk
from tkinter import font

from grafosAciclicos import ventanaAciclico
from gradoNodo import dibujar_grafo
from grafo import ventana_queEs
from grafoDirigido import ventanaDirigido
from grafoNoDirigido import ventanaNoDirigido
from grafoRegular import ventanaRegular
from grafoCompleto import ventanaCompleto
from grafosBipartitos import ventanaBipartito
from matrices import ventanaMatrices
from simple import ventanaSimple


def introduction_grafos():
    ventana = tk.Tk()
    ventana.geometry("600x400")
    ventana.title("Introducción a la Teoría de Grafos")

    # Fuente personalizada
    font_title = font.Font(family="Malgun Gothic", size=16, weight="bold")
    font_body = font.Font(family="Malgun Gothic", size=12)

    # Título
    label_title = tk.Label(
        ventana, 
        text="Introducción a la Teoría de Grafos", 
        font=font_title
    )
    label_title.pack(pady=20)

    # Botones
    buttons = [
        ("Definición de Grafo", ventana_queEs),
        ("Grafos dirigidos", ventanaDirigido),
        ("Grafos no dirigidos", ventanaNoDirigido),
        ("Grafos acíclicos", ventanaAciclico),
        ("Grafos completos", ventanaCompleto),
        ("Grafos regulares", ventanaRegular),
        ("Grafos bipartitos", ventanaBipartito),
        ("Grado de un nodo", dibujar_grafo),
        ("Matrices Adyacencia/Incidencia", ventanaMatrices),
        ("Grafos Simples", ventanaSimple)
    ]

    for i, (text, command) in enumerate(buttons):
        button = tk.Button(
            ventana,
            bg="#80DAEB",
            text=text, 
            font=font_body, 
            command=lambda cmd=command: cmd(ventana)
        )
        button.pack(pady=5)
        button.place(x=100 if i % 2 == 0 else 400, y=100 + (i // 2) * 50)

    ventana.mainloop()

