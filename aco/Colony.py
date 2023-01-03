from aco.ant import Ant


class Colony:
    def __init__(self, parameters, graph):
        self.params = parameters
        self.graph = graph
        self.ants = [Ant(self.graph, self.params)
                     for i in range(self.params.num_ants)]

    def update_colony(self):
        """
        ルートに蓄積するフェロモン量を更新する
        """
        self.__construct_ants()
        self.__calc_passed_pheromone()

    def __construct_ants(self):
        for ant in self.ants:
            ant.construct_routes()

    def __calc_passed_pheromone(self):
        for ant in self.ants:
            ant.calc_passed_pheromone()
