from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as vtx
 
 
def new_graph(order):
    """
    Crea un grafo dirigido vacío.
 
    El grafo tiene los siguientes atributos:
 
    - **vertices**: Mapa (map_linear_probing) con los vértices. Llave: llave del vértice.
    - **num_edges**: Número de arcos del grafo. Se inicializa en 0.
 
    :param order: Número esperado de vértices del grafo
    :type order: int
 
    :returns: Grafo recién creado
    :rtype: digraph
    """
    graph = {
        "vertices": mp.new_map(order, 0.5),
        "num_edges": 0,
    }
    return graph
 
 
def insert_vertex(my_graph, key_u, info_u):
    """
    Inserta un vértice con llave ``key_u`` e información ``info_u`` en el grafo.
    Si el vértice ya existe, se reemplaza.
 
    :returns: Grafo con el vértice insertado
    :rtype: digraph
    """
    new_vertex = vtx.new_vertex(key_u, info_u)
    my_graph["vertices"] = mp.put(my_graph["vertices"], key_u, new_vertex)
    return my_graph
 
 
def contains_vertex(my_graph, key_u):
    """
    Indica si el vértice con llave ``key_u`` existe en el grafo.
 
    :returns: True si el vértice existe, False en caso contrario
    :rtype: bool
    """
    return mp.contains(my_graph["vertices"], key_u)
 
 
def add_edge(my_graph, key_u, key_v, weight=1.0):
    """
    Agrega un arco dirigido de ``key_u`` hacia ``key_v`` con peso ``weight``.
    Si el arco ya existe, solo se actualiza su peso (el número de arcos no cambia).
 
    :raises Exception: Si alguno de los dos vértices no existe en el grafo
 
    :returns: Grafo con el arco agregado
    :rtype: digraph
    """
    vertex_u = mp.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    if not contains_vertex(my_graph, key_v):
        raise Exception("El vertice v no existe")
 
    # Solo se cuenta un arco nuevo si no existía antes
    if vtx.get_edge(vertex_u, key_v) is None:
        my_graph["num_edges"] += 1
 
    vtx.add_adjacent(vertex_u, key_v, weight)
    return my_graph
 
 
def order(my_graph):
    """
    Retorna el orden del grafo (número de vértices).
 
    :rtype: int
    """
    return mp.size(my_graph["vertices"])
 
 
def size(my_graph):
    """
    Retorna el tamaño del grafo (número de arcos).
 
    :rtype: int
    """
    return my_graph["num_edges"]
 