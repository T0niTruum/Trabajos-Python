import networkx as nx


def conectividad(G, nodo):
    """
    Función que retorna la conectividad de un nodo en un grafo.
    Parámetros:
    G: Grafo
    nodo: Nodo del grafo
    Retorna:
    conectividad: Lista con los nodos conectados al nodo
    """
    conectividad = list(G.neighbors(nodo))
    return conectividad
