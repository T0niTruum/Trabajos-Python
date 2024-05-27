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
    ventana.configure(bg="#ffffff")  # Fondo gris claro

    # Fuente personalizada
    font_title = font.Font(family="Malgun Gothic", size=14, weight="bold")
    font_body = font.Font(family="Malgun Gothic", size=12)

    titulo = tk.Label(
        ventana, 
        text="Presentado por:\nJean Kenneth Méndez Cuarán",
        font=font_title,
        bg="#eeeeee",
        fg="#333333"
    )
    titulo.pack(pady=20)  # Espacio superior e inferior

    presentado = tk.Label(
        ventana, 
        text="Presentado a:\nPedro Pablo Cardenas Alzate. Ph.D",
        font=font_body,
        bg="#eeeeee",
        fg="#333333"
    )
    presentado.pack(pady=10)

    cabeza = tk.Label(
        ventana, 
        text="Elija un tema de aprendizaje:", 
        font=font_title,
        bg="#eeeeee",
        fg="#333333"
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