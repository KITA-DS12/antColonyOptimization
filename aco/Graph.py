class Graph:
    def __init__(self, parameters):
        self.params = parameters
        self.coordinates = [None] * self.params.num_vertex
        self.length_edge = [[0 for _ in range(self.params.num_vertex)]
                            for _ in range(self.params.num_vertex)]
        self.pheromone_edge = [[0 for _ in range(self.params.num_vertex)]
                               for _ in range(self.params.num_vertex)]
        self.next_pheromone_edge = [[0 for _ in range(self.params.num_vertex)]
                                    for _ in range(self.params.num_vertex)]
        self.heuristics_edge = [[0 for _ in range(self.params.num_vertex)]
                                for _ in range(self.params.num_vertex)]
