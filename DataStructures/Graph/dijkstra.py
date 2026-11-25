from DataStructures.Graph import digraph as G
from DataStructures.Graph import edge
from DataStructures.Graph import dijsktra_structure as dijk_st
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Stack import stack


def dijkstra(my_graph, source):
    """
    Algoritmo de Dijkstra: calcula los caminos de costo mínimo desde el
    vértice ``source`` hacia todos los vértices alcanzables del grafo.

    En el mapa ``visited`` se guarda, por cada vértice alcanzado, un diccionario
    con ``dist_to`` (mejor distancia conocida), ``edge_to`` (vértice anterior en
    el camino) y ``done`` (True cuando su distancia ya es definitiva).

    Para evitar la búsqueda lineal de ``improve_priority``, cuando se encuentra
    una mejor distancia se inserta una nueva entrada en la cola y las entradas
    viejas se ignoran al sacarlas (el vértice ya estará ``done``).

    :raises Exception: Si el vértice ``source`` no existe

    :returns: Estructura de búsqueda con ``source``, ``visited`` y ``pq``
    :rtype: dijsktra_search
    """
    if not G.contains_vertex(my_graph, source):
        raise Exception("El vertice source no existe")

    search = dijk_st.new_dijsktra_structure(source, G.order(my_graph))
    visited = search["visited"]
    heap = search["pq"]

    mp.put(visited, source, {"dist_to": 0, "edge_to": None, "done": False})
    pq.insert(heap, 0, source)

    while not pq.is_empty(heap):
        v = pq.remove(heap)
        info_v = mp.get(visited, v)
        if info_v["done"]:
            continue  # entrada vieja: ya se encontró un camino mejor
        info_v["done"] = True
        dist_v = info_v["dist_to"]

        edges = G.edges_vertex(my_graph, v)
        for i in range(lt.size(edges)):
            arc = lt.get_element(edges, i)
            w = edge.to(arc)
            new_dist = dist_v + edge.weight(arc)
            info_w = mp.get(visited, w)
            if info_w is None:
                mp.put(visited, w, {"dist_to": new_dist, "edge_to": v, "done": False})
                pq.insert(heap, new_dist, w)
            elif not info_w["done"] and new_dist < info_w["dist_to"]:
                info_w["dist_to"] = new_dist
                info_w["edge_to"] = v
                pq.insert(heap, new_dist, w)
    return search


def has_path_to(key_v, search):
    """
    Indica si existe un camino desde ``source`` hasta ``key_v``.

    :rtype: bool
    """
    return mp.contains(search["visited"], key_v)


def dist_to(key_v, search):
    """
    Retorna la distancia mínima desde ``source`` hasta ``key_v``.
    Retorna infinito (float('inf')) si no hay camino.

    :rtype: float
    """
    info = mp.get(search["visited"], key_v)
    if info is None:
        return float("inf")
    return info["dist_to"]


def path_to(key_v, search):
    """
    Retorna una pila (stack) con el camino de costo mínimo desde ``source``
    hasta ``key_v`` (el tope de la pila es ``source``). Retorna None si no
    hay camino.

    :rtype: stack
    """
    if not has_path_to(key_v, search):
        return None

    path = stack.new_stack()
    current = key_v
    while current != search["source"]:
        stack.push(path, current)
        current = mp.get(search["visited"], current)["edge_to"]
    stack.push(path, search["source"])
    return path