import random as rnd


class Node:
    def __init__(self, name, coords, adjacents):
        self.name = name

        self.coords = coords
        if coords == [-1, -1]:
            self.coords = [
                round(rnd.uniform(10, 50), 1),
                round(rnd.uniform(10, 50), 1),
            ]

        self.adjacents = adjacents
        if adjacents != []:
            # n-1 to account for the starting line number that is 1 in the .data
            self.adjacents = [int(n.strip("\n")) - 1 for n in adjacents]


class Vertex:
    def __init__(self, node1, node2):
        self.dir = (
            node2.coords[0] - node1.coords[0],
            node2.coords[1] - node1.coords[1],
        )
        self.a = self.dir[1]
        self.b = -1 * self.dir[0]

    def Intersect(self, other, bounding_box):
        epsilon = 1e-3

        # Intersection at infinity
        if other.a - self.a < epsilon:
            return False

        x = (other.b - self.b) / (other.a - self.a)
        y = self.a * x + self.b

        return bounding_box.Contain(x, y)
