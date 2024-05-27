import matplotlib.pyplot as plt
import networkx as nx


def es_fuertemente_conexo(G):
    if nx.is_strongly_connected(G):
        print("El grafo es fuertemente conexo.")
        return True
    else:
        print("El grafo no es fuertemente conexo.")
        return False


def dibujar_grafo():
    # Crear un grafo vacío (dirigido)
    es_dirigido = input("¿Quieres un grafo dirigido? (s/n): ").lower() == "s"
    G = nx.DiGraph()

    # Agregar nodos
    num_nodos = int(input("Ingresa el número de nodos: "))
    for i in range(num_nodos):
        G.add_node(i)

    # Agregar aristas (enlaces)
    while True:
        u = int(input("Ingresa el nodo de origen (0-{0}): ".format(num_nodos - 1)))
        v = int(input("Ingresa el nodo de destino (0-{0}): ".format(num_nodos - 1)))
        G.add_edge(u, v)

        continuar = input("¿Agregar otra arista? (s/n): ").lower()
        if continuar != "s":
            break

    # Verificar si el grafo es fuertemente conexo
    es_fuertemente_conexo(G)

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
    plt.show()


if __name__ == "__main__":
    dibujar_grafo()