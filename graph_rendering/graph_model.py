from utils import Load_Data, Print_Graph


def Get_Node_Potentiel_Crossing(graph, node_number, vertex_number):
    first_degree_adjacent = graph[node_number].adjacents[vertex_number]

    potential_crossings = []
    for second_degree_adjacent in graph[first_degree_adjacent].adjacents:
        vertex_list = []

        for adj in graph[second_degree_adjacent].adjacents:
            vertex_list.append((
                second_degree_adjacent,
                adj,
            ))

        potential_crossings.extend(vertex_list)

    return (
        (node_number, first_degree_adjacent),
        potential_crossings,
    )


def Get_Crossing_Number(graph):
    pass


graph = Load_Data()
crossings = Get_Node_Potentiel_Crossing(graph, 0, 0)
print(crossings)
Print_Graph(graph)
