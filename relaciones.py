import tkinter as tk

# from dibujar_Bipartito import dibujar_Bipartito


def ventanaRelaciones(ventana):
    
    ventana = tk.Tk()
    ventana.title("Relaciones")
    ventana.geometry("500x500")
    texto = "Las relaciones se refieren a la existencia de aristas entre dos vertices "
    texto1="\n\nHay 3 tipos de relaxiones: \n -Asimetrica: La relacion entre los vertices es unidireccional, no reciproca\n si hay una Arista de A a B, no puede haber una de B a A"
    texto2="\n-Simetrica: Si existe una relacion de A a B, implica que existe una de B a A"
    texto3="\n-Nula: Es la ausencia de una arista entre dos nodos"
    texto4="\n\nEn los Grafos no dirigidos las aristas representan relaciones simetricas por naturaleza\n mientras que en los dirigidos si es posible saber la direccion"


    label = tk.Label(ventana, text=texto+texto1+texto2+texto3+texto4)
    label.pack()

    # img_path = "images/grafosRegulares-removebg-preview(1).png"
    # img_pil = Image.open(img_path)
    # img_tk = ImageTk.PhotoImage(img_pil)
 
    # canvas = tk.Canvas(ventana, width=img_pil.width, height=img_pil.height)
    # canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    # canvas.pack()

    # button = tk.Button(
    #     ventana, text="Dibujar grafo", command=lambda: dibujar_Bipartito(), fg="red"
    # )
    # button.pack()
    # button.place(x=200, y=400)


    ventana.mainloop()

    return ventana