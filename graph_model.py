import random as rnd
import matplotlib.pyplot as plt


def Load_Data():
    graph = []

    with open("graph.data", "r") as f:
        line = f.readline()

        while line:
            node_data = line.split("  ")
            node_name = node_data[0]
            node_coords = [float(c) for c in node_data[1].split(" ")]

            if node_coords == [-1, -1]:
                node_coords = [
                    round(rnd.uniform(10, 50), 1),
                    round(rnd.uniform(10, 50), 1),
                ]

            # n-1 to account for the starting line number that is 1 in the .data
            node_neighbours = (
                [int(n.strip("\n")) - 1 for n in node_data[2].split(" ")]
                if len(node_data) == 3
                else []
            )

            graph.append({
                "name": node_name,
                "coords": node_coords,
                "adjacents": node_neighbours,
            })
            line = f.readline()

    return graph


def Print_Graph(graph):
    for node in graph:
        plt.text(node["coords"][0], node["coords"][1], node["name"])
        plt.plot(node["coords"][0], node["coords"][1], "ko")

    plt.show()


def Get_Node_Potentiel_Crossing(graph, node_number, vertex_number):
    first_degree_adjacent = graph[node_number]["adjacents"][vertex_number]

    potential_crossings = []
    for second_degree_adjacent in graph[first_degree_adjacent]["adjacents"]:
        vertex_list = []

        for adj in graph[second_degree_adjacent]["adjacents"]:
            vertex_list.append((
                second_degree_adjacent,
                adj,
            ))

        potential_crossings.extend(vertex_list)

    return (
        (node_number, first_degree_adjacent),
        potential_crossings,
    )


graph = Load_Data()
crossings = Get_Node_Potentiel_Crossing(graph, 0, 0)
print(crossings)
Print_Graph(graph)
