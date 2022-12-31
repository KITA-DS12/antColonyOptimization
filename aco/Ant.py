class Ant:
    def __init__(self, parameters, graph):
        self.params = parameters
        self.graph = graph
        self.visited_routes = []
        self.visited_vertexes = [False for _ in range(self.params.num_vertexes)]
        self.init_vertex = self.params.initial_vertex
