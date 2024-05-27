import tkinter as tk
from PIL import Image, ImageTk

from dibujarSimple import dibujar_Simple


def ventanaSimple(ventana):
    
    ventana = tk.Tk()
    ventana.title("Grafo Simple")
    ventana.geometry("500x250")
    texto = "Un grafo Simple es aquel que no tiene aristas paralelas ni ciclicas"

    label = tk.Label(ventana, text=texto, wraplength=480)
    label.pack()

    # img_path = "images/grafosRegulares-removebg-preview(1).png"
    # img_pil = Image.open(img_path)
    # img_tk = ImageTk.PhotoImage(img_pil)
 
    # canvas = tk.Canvas(ventana, width=img_pil.width, height=img_pil.height)
    # canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    # canvas.pack()

    button = tk.Button(
        ventana, text="Dibujar grafo", command=lambda: dibujar_Simple(), fg="red"
    )
    button.pack()
    button.place(x=200, y=100)


    ventana.mainloop()

    return ventana