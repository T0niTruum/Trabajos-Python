import tkinter as tk
import tkinter as tk

from hamiltoniano import dibujarGrafoHamilton
from koningsberg import definicionProblema
from ventanaEuler import crear_ventana_euler


def euler_ventana_grafo(ventana):
    crear_ventana_euler()


def crear_ventana():
    ventana = tk.Tk()  # Llama al constructor Tk() para crear la ventana
    ventana.title("Conexidad")  # Proporciona un título entre las comillas
    ventana.geometry("100x100")  # tamaño de la ventana

    # Estilo de fuente
    font = ("Malgun Gothic", 12)

    # Estilo de los botones
    button_style = {
        "font": font,
        "bg": "#80DAEB",  # Verde
        "fg": "white",    # Texto blanco
        "relief": "raised",
        "borderwidth": 3,
        "width": 25,
        "height": 1,
    }

    # Título
    title_label = tk.Label(ventana, text="Seleccione una opción:", font=("Malgun Gothic", 16))
    title_label.pack(pady=20)

    buttoneuler = tk.Button(
        ventana, text="Grafo Euleriano", command=lambda: euler_ventana_grafo(ventana), **button_style
    )
    buttoneuler.pack(pady=10)

    button_hamilton = tk.Button(
        ventana, text="Grafo Hamiltoniano", command=dibujarGrafoHamilton, **button_style
    )
    button_hamilton.pack(pady=10)

    button_koonisber = tk.Button(
        ventana, text="Puentes de Konisberg", command=definicionProblema, **button_style
    )
    button_koonisber.pack(pady=10)

    return ventana
