import tkinter as tk

from PIL import Image, ImageTk


def introduccion_grafo_euleriano():
    parte1 = "Un circuito euleriano es un circuito simple que recorre todas las aristas del grafo"
    parte2 = "un grafo que admite un circuito euleriano se llama grafo euleriano"
    parte3 = "Un grafo euleriano es aquel grafo que permite recorrer todas sus aristas una sola vez y regresar al punto de partida"
    parte4 = "Un grafo conexo es euleriano si y solo si todos sus vértices son de grado par\n"
    return parte1 + "\n" + parte2 + "\n" + parte3 + "\n" + parte4


def introduccion_camino_euleriano():
    texto = "UN camino eulerinaoi es un camino simple que recorre todas las aristas del grafo\n"
    parte1 = "Un grafo no eulerinao es que permite un camino euleriano se llama semi-euleriano\n"
    texto = texto + parte1
    return texto


def ventanas_grafos_eulerianos():
    ventana = tk.Tk()

    # Título para la sección de introducción al Grafo Euleriano
    titulo_grafo_euleriano = tk.Label(
        ventana, text="Introducción al Grafo Euleriano", font=("Arial", 14, "bold")
    )
    titulo_grafo_euleriano.pack()

    # Contenido para la sección de introducción al Grafo Euleriano
    parte_1_grafo_euleriano = tk.Label(
        ventana, text=introduccion_grafo_euleriano(), font=("Arial", 12)
    )
    parte_1_grafo_euleriano.pack()

    # Imagen para la sección de introducción al Grafo Euleriano
    # imagen_1 = Image.open("imagen_grafo_euleriano.png")
    # imagen_1 = imagen_1.resize((200, 200), Image.ANTIALIAS)
    # imagen_1 = ImageTk.PhotoImage(imagen_1)
    # label_imagen_1 = tk.Label(ventana, image=imagen_1)
    # label_imagen_1.pack()

    # Título para la sección de introducción al Camino Euleriano
    titulo_camino_euleriano = tk.Label(
        ventana, text="Introducción al Camino Euleriano", font=("Arial", 14, "bold")
    )
    titulo_camino_euleriano.pack()

    # Contenido para la sección de introducción al Camino Euleriano
    parte_2_camino_euleriano = tk.Label(
        ventana, text=introduccion_camino_euleriano(), font=("Arial", 12)
    )
    parte_2_camino_euleriano.pack()

    # Imagen para la sección de introducción al Camino Euleriano
    # imagen_2 = Image.open("imagen_camino_euleriano.png")
    # imagen_2 = imagen_2.resize((200, 200), Image.ANTIALIAS)
    # imagen_2 = ImageTk.PhotoImage(imagen_2)
    # label_imagen_2 = tk.Label(ventana, image=imagen_2)
    # label_imagen_2.pack()

    return ventana