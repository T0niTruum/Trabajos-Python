from tkinter import simpledialog,messagebox
import matplotlib.pyplot as plt
import networkx as nx



def esHamiltoniano(G,ax2):
    # Verificamos si es dirigido o no
    if nx.is_directed(G):

        #verificamos si el grafo tiene conexidad debil
        if nx.is_weakly_connected(G):
            text = "El grafo no es Hamiltoniano\n ni tiene camino Hamiltoniano \nporque es débilmente conexo"
            ax2.text(0.5, 0.5, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
            return False
    else:
        # verificamos si el grafo es conexo
        if not nx.is_connected(G):
           
            #ponemos el texto en la segunda figura "ax2"
            text = "El grafo no es Hamiltoniano \n ni tiene un camino Hamiltoniano \nporque no es conexo"
            ax2.text(0.5, 0.5, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
            return False
        
        n = G.number_of_nodes()
        if(n>3):
            #Agrego el texto
            text = "según el teorema de Dirac si G es conexo,\n tiene mas de 3 vertices y cada vertice 'v' de G \n cumple que deg(v)>=|V|/2\n su grado es mayor o igual al total de vertices dividido entre dos\nEl grafo es Hamiltoniano"
            ax2.text(0.5, 1, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
            
            # verificamos si se cumple el teorema de Dirac
            if all(deg >= n / 2 for _, deg in G.degree()):
            
                text = "El grafo es Hamiltoniano\n porque cumple el teorema de Dirac"
                ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
                return True
            else:
        
                text = "El grafo no es Hamiltoniano\n porque no cumple el teorema de Dirac"
                ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
                return False
    

def caminoHamiltoniano(G):
    n = len(G)
    visitado = [False] * n
    camino = []

    def recorrer(node):
        visitado[node] = True
        camino.append(node)

        if len(camino) == n:
            return True
        

        for vecino in G[node]:
            if not visitado[vecino]:
                if recorrer(vecino):
                    return True

        visitado[node] = False
        camino.pop()
        return False

    for node in range(n):
        if recorrer(node):
            return True

    return False

def dibujarGrafoHamilton():

    # Crear una ventana con dos subfiguras
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    #quitamos el grafico generado automaticamente
    ax2.axis("off")

    es_dirigido = messagebox.askyesno(
        "Tipo de grafo", "¿Quieres un grafo dirigido? (s/n):"
    )
    G = nx.DiGraph() if es_dirigido else nx.Graph()

    # Agregar nodos
    num_nodos = simpledialog.askinteger("Nodos","ingresa el numero de nodos:")
    if num_nodos is None:
        return
    
    for i in range(num_nodos):
        G.add_node(i)

    # Agregar aristas (enlaces)
    while True:
        u=simpledialog.askinteger("Aristas","Ingresa el nodo de origen (0-{0}): ".format(num_nodos - 1))
        v=simpledialog.askinteger("Aristas","Ingresa el nodo de destino (0-{0}): ".format(num_nodos - 1))
        
        G.add_edge(u, v)
        
        continuar = messagebox.askyesno(
        "Arista", "¿Quieres otra arista? (s/n):"
    )
        if not continuar:
            break

    opcion = simpledialog.askinteger("Que deseas verificar","1. Si es hamiltoniano\n2. Si tiene un camino Hamiltoniano")

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    #creamos el grafo en ax1
    nx.draw(G, pos,ax=ax1,with_labels=True, node_size=500, node_color="skyblue", font_size=10)


    if opcion == 1:
        nx.draw_networkx_edges(G, pos,ax=ax1, width=2, alpha=0.5, edge_color="r")
        esHamiltoniano(G,ax2)
    elif opcion == 2:
        nx.draw_networkx_edges(G, pos,ax=ax1, width=2, alpha=0.5, edge_color="r")
        if caminoHamiltoniano(G):
            text = "El grafo tiene un camino Hamiltoniano"
        else:
            text ="El grafo no tiene un camino Hamiltoniano"
        ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12) 
    plt.show()


if __name__ == "__main__":
    dibujarGrafoHamilton()