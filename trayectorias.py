import tkinter as tk

# from dibujar_Bipartito import dibujar_Bipartito


def ventanaTrayectoria(ventana):
    
    ventana = tk.Tk()
    ventana.title("Trayectorias")
    ventana.geometry("500x500")
    texto = "Es la secuencia de vertices adyacentes recorridos,\n es decir que cada vertice consecutivo que se recorre esta conectado por una arista"
    texto1="\n\n-se pueden repetir nodos o vertices pero no aristas y su longitud es igual a la cantidad de aristas que recorrio"
    texto2="\n-Las trayectorias son utiles para comprender la conectividad entre vertices y las propiedades y estructura de un grafo"

    label = tk.Label(ventana, text=texto+texto1+texto2)
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