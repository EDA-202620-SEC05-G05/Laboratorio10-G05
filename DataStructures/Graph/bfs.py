from DataStructures.Graph import digraph as G
from DataStructures.Graph import bfs_structure as bfs_st
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue
from DataStructures.Stack import stack


def bfs(my_graph, source):
    """
    Recorrido en amplitud (BFS) del grafo desde el vértice ``source``.

    :raises Exception: Si el vértice ``source`` no existe

    :returns: Estructura de búsqueda con ``marked`` y ``edge_to``
    :rtype: bfs_search
    """
    if not G.contains_vertex(my_graph, source):
        raise Exception("El vertice source no existe")

    search = bfs_st.new_bfs_structure(source, G.order(my_graph))
    mp.put(search["marked"], source, True)
    bfs_vertex(my_graph, source, search)
    return search


def bfs_vertex(my_graph, source, search):
    """
    Recorre por niveles el grafo a partir de ``source`` usando una cola.
    Cada vértice se marca al ser encolado, para no encolarlo dos veces.

    :returns: Estructura de búsqueda actualizada
    :rtype: bfs_search
    """
    pending = queue.new_queue()
    queue.enqueue(pending, source)

    while not queue.is_empty(pending):
        current = queue.dequeue(pending)
        adj = G.adjacents(my_graph, current)
        for i in range(lt.size(adj)):
            w = lt.get_element(adj, i)
            if not mp.contains(search["marked"], w):
                mp.put(search["marked"], w, True)
                mp.put(search["edge_to"], w, current)
                queue.enqueue(pending, w)
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