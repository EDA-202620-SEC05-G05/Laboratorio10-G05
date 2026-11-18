import sys

from DataStructures.Graph import digraph as G
from DataStructures.Graph import dfs_structure as dfs_st
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt
from DataStructures.Stack import stack


def dfs(my_graph, source):
    """
    Recorrido en profundidad (DFS) del grafo desde el vértice ``source``.

    :raises Exception: Si el vértice ``source`` no existe

    :returns: Estructura de búsqueda con ``marked`` y ``edge_to``
    :rtype: dfs_search
    """
    if not G.contains_vertex(my_graph, source):
        raise Exception("El vertice source no existe")

    # DFS es recursivo: se sube el límite para grafos grandes
    needed = G.order(my_graph) + 1000
    if sys.getrecursionlimit() < needed:
        sys.setrecursionlimit(needed)

    search = dfs_st.new_dfs_structure(source, G.order(my_graph))
    mp.put(search["marked"], source, True)
    dfs_vertex(my_graph, source, search)
    return search


def dfs_vertex(my_graph, key_v, search):
    """
    Visita recursivamente los adyacentes no marcados de ``key_v``.

    :returns: Estructura de búsqueda actualizada
    :rtype: dfs_search
    """
    adj = G.adjacents(my_graph, key_v)
    for i in range(lt.size(adj)):
        w = lt.get_element(adj, i)
        if not mp.contains(search["marked"], w):
            mp.put(search["marked"], w, True)
            mp.put(search["edge_to"], w, key_v)
            dfs_vertex(my_graph, w, search)
    return search


def has_path_to(key_v, search):
    """
    Indica si existe un camino desde ``source`` hasta ``key_v``.

    :rtype: bool
    """
    return mp.contains(search["marked"], key_v)


def path_to(key_v, search):
    """
    Retorna una pila (stack) con el camino desde ``source`` hasta ``key_v``
    (el tope de la pila es ``source``). Retorna None si no hay camino.

    :rtype: stack
    """
    if not has_path_to(key_v, search):
        return None

    path = stack.new_stack()
    current = key_v
    while current != search["source"]:
        stack.push(path, current)
        current = mp.get(search["edge_to"], current)
    stack.push(path, search["source"])
    return path