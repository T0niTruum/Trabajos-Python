import tkinter as tk

def ventana_queEs(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("Definición de Grafo")
    ventana.geometry("300x75")
    texto = "Pareja ordenada de la forma G(V,A).\nV representa un conjunto de vértices o nodos.\nA representa un conjunto de aristas."
    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    ventana.mainloop()

    return ventana
