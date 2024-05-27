import tkinter as tk
from PIL import Image, ImageTk

from dibujarSimple import dibujar_Simple


def ventanaSimple(ventana):
    
    ventana = tk.Tk()
    ventana.title("Grafo Simple")
    ventana.geometry("350x100")
    ventana.configure(bg="#d2f4e4")
    texto = "Grafo que no presenta aristas paralelas ni bucles en su topología"

    label = tk.Label(ventana, bg="#d2f4e4",text=texto, wraplength=480)
    label.pack()

    # img_path = "images/grafosRegulares-removebg-preview(1).png"
    # img_pil = Image.open(img_path)
    # img_tk = ImageTk.PhotoImage(img_pil)
 
    # canvas = tk.Canvas(ventana, width=img_pil.width, height=img_pil.height)
    # canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    # canvas.pack()

    button = tk.Button(
        ventana, foreground="white", background="#80DAEB", text="Dibujar grafo", command=lambda: dibujar_Simple()
    )
    button.pack(pady=15)


    ventana.mainloop()

    return ventana