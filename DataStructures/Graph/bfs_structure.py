from DataStructures.Map import map_linear_probing as mp


def new_bfs_structure(source, g_order):
    """
    Crea una estructura de búsqueda usada en el algoritmo **bfs**.

    - **source**: Vértice de origen.
    - **marked**: Mapa con los vértices visitados.
    - **edge_to**: Mapa con el vértice desde el cual se llegó a cada vértice.

    :rtype: bfs_search
    """
    structure = {
        "source": source,
        "marked": mp.new_map(g_order, 0.5),
        "edge_to": mp.new_map(g_order, 0.5),
    }
    return structure