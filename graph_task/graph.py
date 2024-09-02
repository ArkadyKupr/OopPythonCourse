class Graph:
    def __init__(self):
        self.__nodes = {}

    def add_node(self, value):
        if value not in self.__nodes:
            self.__nodes[value] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.__nodes:
            if to_node in self.__nodes:
                self.__nodes[from_node].append(to_node)

    def print_graph(self):
        for value in self.__nodes.values():
            print(value)

    def graph_matrix(self):
        dimension = len(self.__nodes)

        matrix = [None] * dimension

        for element in matrix:
            element = [False] * dimension
