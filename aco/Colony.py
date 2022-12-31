from aco.ant import Ant


class Colony:
    def __init__(self, parameters, graph):
        self.params = parameters
        self.graph = graph
        self.ants = [Ant(self.graph, self.params)
                     for i in range(self.params.num_ants)]
