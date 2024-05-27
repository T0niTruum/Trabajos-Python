import os
import tkinter as tk


def definicionProblema():
    parte1 = "Los puentes de koningsberg fueron un problema matemático que se planteó en el siglo XVIII y que fue resuelto por Leonhard Euler en 1735.\n"
    parte2 = "El problema consiste en determinar si es posible recorrer todos los puentes de la ciudad de Konisberg, cruzando cada uno de ellos una sola vez y volviendo al punto de partida.\n "
    parte3 = "La ciudad de Konisberg estaba dividida en cuatro zonas por el río Pregel y siete puentes la unían.\n"
    parte4 = "Euler demostró que esto no era posible y que, por lo tanto, no existía un camino que recorriera todos los puentes de la ciudad sin cruzar ninguno de ellos más de una vez.\n"
    parte5 = "para resolver el problema, Euler representó la ciudad de Konisberg como un grafo, es decir, un conjunto de nodos (las zonas de la ciudad) y aristas (los puentes que las unen).\n  "
    parte6 = "En este grafo, cada nodo representa una zona de la ciudad y cada arista representa un puente.\n"
    parte7 = "Euler demostró que, para que exista un camino que recorra todos los puentes de la ciudad sin cruzar ninguno de ellos más de una vez, es necesario que todos los nodos del grafo tengan un número par de aristas que los unan.\n"
    parte8 = " En el caso de la ciudad de Konisberg, dos de los nodos tenían un número impar de aristas que los unían, por lo que no era posible recorrer todos los puentes de la ciudad sin cruzar ninguno de ellos más de una vez.\n"
    window = tk.Tk()
    window.title("Puentes de Koningsberg")
    window.geometry("1300x150")
    window.configure(bg="#d2f4e4")

    label = tk.Label(
        window,
        bg="#d2f4e4",
        text=parte1 + parte2 + parte3 + parte4 + parte5 + parte6 + parte7 + parte8,
    )
    label.pack()

    # image_path = os.path.join(os.path.dirname(__file__), 'images', 'images.jpg')
    image = tk.PhotoImage(file="")

    
    #label1 = tk.Label(
     #   window,
      #  text="Un puente de Konisberg es un grafo que tiene 4 nodos y 7 aristas",
       # image=image,
    #)
    #label1.pack()

    # window.mainloop()
    return window