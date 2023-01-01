class Graph:
    def __init__(self, parameters):
        self.params = parameters
        self.coordinates = [None] * self.params.num_node
        self.length_edge = [[0 for _ in range(self.params.num_node)]
                            for _ in range(self.params.num_node)]
        self.pheromone_edge = [[0 for _ in range(self.params.num_node)]
                               for _ in range(self.params.num_node)]
        self.next_pheromone_edge = [[0 for _ in range(self.params.num_node)]
                                    for _ in range(self.params.num_node)]
        self.heuristics_edge = [[0 for _ in range(self.params.num_node)]
                                for _ in range(self.params.num_node)]
