import networkx as nx


def teorema_del_apreton(G):
    """
    Calcula el número de apretones de manos que se dan en una reunión.
    """
    respuesta = ""
    numero_nodos = G.degree()
    numero_aristas = G.number_of_edges()
    numero_aristas = numero_aristas * 2
    if numero_nodos == numero_aristas:
        respuesta = "Según el teorema del apretón de manos, el número de nodos es igual al doble de aristas"
    else:
        respuesta = "Según el teorema del apretón de manos, el número de nodos no es igual al doble de aristas por lo que no se cumple en este grafo"
    return respuesta
