import bisect
import random


class Ant:
    def __init__(self, parameters, graph):
        self.params = parameters
        self.graph = graph
        self.visited_routes = [self.params.initial_node]
        self.visited_nodes = [
            False for _ in range(self.params.num_node)]
        self.visited_nodes[self.params.initial_node] = True

    def construct_routes(self):
        """
        アリの移動するルートを構築する
        """
        for _ in range(self.params.num_node-1):
            # 現在のノード
            v = self.params.visited_routes[-1]
            # ノードvから移動できるノードと確率
            to_nodes, to_probabilitys = self.__calc_probability_from_v(v)
            # 確率選択
            random_probability = random.uniform(0.0, 0.999999999)
            to_node = to_nodes[bisect.bisect_left(
                to_probabilitys, random_probability)]
            # to_nodeへ移動
            self.visited_routes.append(to_node)
            self.visited_nodes[to_node] = True

    def __calc_probability_from_v(self, v):
        """
        現在のノードvから移動できる各ノードを選択する確率を求める

        Parameters
        ----------
        v: int
            現在のノードに該当するインデックス

        Returns
        -------
        to_nodes: list
            ノードvから移動できるノード群
        to_probablitys: list
            ノードvから移動できる各ノードを選択する確率の累積和
        """

        # 移動できるノードにおける確率の合計
        sum_probablity = 0

        # 移動できるルート
        to_nodes = []
        # 移動できるルートのフェロモン量
        to_pheromones = []

        for to in range(self.params.num_node):
            # 現在のノードまたは既に訪れたノードはスキップ
            if (to == v) or self.params.visited_nodes[to]:
                continue
            """
            self.graph.pherome_edge[v][to] : tau(v,to)
                ノードv, to間のエッジ(v,to)に蓄積するフェロモン量
            self.graph.heuristics_edge[v][to] : eta(v,to)
                ノードv, to間のエッジ(v,to)のヒューリスティック値
            """
            # フェロモン量 * ヒューリスティック値
            pheromone = (self.graph.pheromone_edge[v][to] ** self.params.alpha)
            * (self.graph.heuristics_edge[v][to] ** self.params.beta)

            sum_probablity += pheromone
            to_nodes.append(to)
            to_pheromones.append(pheromone)
        # 各ノードが選ばれる確率
        to_probablitys = [p / sum_probablity for p in to_pheromones]
        # to_probablitysの累積和
        for i in range(len(to_probablitys) - 1):
            to_probablitys[i+1] += to_probablitys[i]

        return to_nodes, to_probablitys
