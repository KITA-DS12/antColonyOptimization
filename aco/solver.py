from aco.parameters import Parameters
from aco.graph import Graph
from aco.colony import Colony


class Solver:
    def __init__(self, num_ant, num_node, q, alpha, beta, rou,
                 max_iteration, initial_node, min_tau, max_tau):
        self.params = Parameters(num_ant, num_node, q, alpha, beta, rou,
                                 max_iteration, initial_node, min_tau, max_tau)
        self.graph = Graph(self.params)
        self.colony = Colony(self.params, self.graph)

    def __update_aco(self):
        self.colony.update_colony()
        self.__update_next_pheromones()

    def __update_next_pheromones(self):
        """
        ルートに蓄積するフェロモン量を更新する
        """
        # 現在のフェロモン * 蒸発率(rou) + 新たに分泌されたフェロモン
        for i in range(self.paramas.num_node):
            for j in range(self.params.num_node):
                self.graph.pheromone_edge[i][j] = \
                    self.graph.pheromone_edge[i][j] * self.params.rou \
                    + self.graph.next_pheromone_edge[i][j]

        # 上限(tau_max), 下限(tau_min)を適用する
        for i in range(self.paramas.num_node):
            for j in range(self.params.num_node):
                self.graph.pheromone_edge[i][j] = \
                    min(self.params.tau_max,
                        max(self.graph.pheromone_edge[i][j],
                            self.params.tau_min))
