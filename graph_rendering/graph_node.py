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
