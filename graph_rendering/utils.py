import matplotlib.pyplot as plt
from graph_classes import Node


def Load_Data():
    graph = []

    with open("graph.data", "r") as f:
        line = f.readline()

        while line:
            node_data = line.split("  ")
            node_name = node_data[0]
            node_coords = [float(c) for c in node_data[1].split(" ")]
            node_neighbours = node_data[2].split(" ") if len(node_data) == 3 else []

            node = Node(node_name, node_coords, node_neighbours)
            graph.append(node)
            line = f.readline()

    return graph


def Print_Graph(graph):
    for node in graph:
        plt.text(
            node.coords[0],
            node.coords[1],
            node.name,
            bbox=dict(facecolor="white", alpha=0.5),
        )

        for adj in node.adjacents:
            xs = [node.coords[0], graph[adj].coords[0]]
            ys = [node.coords[1], graph[adj].coords[1]]
            plt.plot(xs, ys, "ko-")

    plt.show()
