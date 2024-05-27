import tkinter as tk
from tkinter import font

from conexidad import crear_ventana
from introduccion import introduction_grafos


def conexidad(ventana):
    crear_ventana()


def introduction(ventana):
    introduction_grafos()


def ventana_crear():
    ventana = tk.Tk()
    ventana.title("Teoría de Grafos")
    ventana.geometry("500x400")
    ventana.configure(bg="#d2f4e4")

    # Fuente personalizada
    font_title = font.Font(family="Malgun Gothic", size=14, weight="bold")
    font_body = font.Font(family="Malgun Gothic", size=12)

    titulo = tk.Label(
        ventana,
        bg="#d2f4e4", 
        text="Estudiante:\nJean Kenneth Méndez Cuarán\nCódigo: 1.120.839.058",
        font=font_body
    )
    titulo.pack(pady=20)  # Espacio superior e inferior

    presentado = tk.Label(
        ventana,
        bg="#d2f4e4",
        text="Pedro Pablo Cardenas Alzate. Ph.D\nDocente",
        font=font_body
    )
    presentado.pack(pady=10)

    cabeza = tk.Label(
        ventana,
        bg="#d2f4e4", 
        text="Temas de aprendizaje:", 
        font=font_title
    )
    cabeza.pack(pady=30)

    button_style = {
        "font": font_body,
        "bg": "#80DAEB",  # Verde
        "fg": "white",
        "activebackground": "#ff0000",
        "activeforeground": "white",
        "width": 30,
        "height": 1,
        "bd": 3,
        "relief": "raised"
    }

    button_introdcution = tk.Button(
        ventana, 
        text="Introducción a la teoría de grafos", 
        command=lambda: introduction(ventana), 
        **button_style
    )
    button_introdcution.pack(pady=10)

    button_conexidad = tk.Button(
        ventana, 
        text="Conexidad", 
        command=lambda: conexidad(ventana), 
        **button_style
    )
    button_conexidad.pack(pady=10)

    ventana.mainloop()


ventana_crear()