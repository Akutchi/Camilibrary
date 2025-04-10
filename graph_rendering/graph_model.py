from utils import Load_Data, Print_Graph
from graph_classes import Vertex


def Get_Node_Potentiel_Crossing(graph, node_number, vertex_number):
    degree_1_adj = graph[node_number].adjacents[vertex_number]

    potential_crossings = []
    for degree_2_adj in graph[degree_1_adj].adjacents:
        vertex_list = []

        for degree_3_adj in graph[degree_2_adj].adjacents:
            vertex_list.append(Vertex(graph[degree_2_adj], graph[degree_3_adj]))

        potential_crossings.extend(vertex_list)

    return (
        Vertex(graph[node_number], graph[degree_1_adj]),
        potential_crossings,
    )


def Get_Bounding_Box(graph, potential_crossings):
    return [0, 0, 0, 0]


def Get_Crossing_Number(graph, potential_crossings):
    bounding_box = Get_Bounding_Box(graph, potential_crossings)

    chosen_vertex = potential_crossings[0]
    crossings = potential_crossings[1]

    crossing_number = 0
    for vertex in crossings:
        crossing_number += chosen_vertex.Intersect(vertex, bounding_box)


graph = Load_Data()
""" crossings = Get_Node_Potentiel_Crossing(graph, 0, 0)
CN = Get_Crossing_Number(graph, crossings) """
Print_Graph(graph)
