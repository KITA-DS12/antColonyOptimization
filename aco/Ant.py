import bisect
import random


class Ant:
    """
    アリを管理する

    Attributes
    ----------
    params: Parameters
        ACOを設定するすべてのパラメータを保存する
    graph: Graph
        ノードの座標やエッジの距離，フェロモン量などを保存する
    visited_routes: list of int
        アリが通ったノードのインデックスを格納する
    is_visited_nodes: list of bool
        アリが既に通ったかを真偽値で格納する
    """

    def __init__(self, parameters, graph):
        """
        Parameters
        ----------
        parameters: Parameters
            ACOを設定するすべてのパラメータを保存する
        graph: Graph
            ノードの座標やエッジの距離，フェロモン量などを保存する
        """
        self.params = parameters
        self.graph = graph
        self.visited_routes = [self.params.start_node]
        self.is_visited_nodes = [
            False for _ in range(self.params.num_node)]
        self.is_visited_nodes[self.params.initial_node] = True

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
            self.is_visited_nodes[to_node] = True

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
            if (to == v) or self.params.is_visited_nodes[to]:
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

    def calc_passed_pheromone(self):
        """
        アリの通ったルートのフェロモン量を計算する
        """
        passed_length = self.calc_length_routes()
        q = self.params.q
        for i in range(self.params.num_node-1):
            self.graph.next_pheromone_edge[
                self.visited_routes[i]][
                self.visited_routes[i+1]
            ] += q/passed_length

    def calc_length_routes(self):
        """
        通ったルートの長さを計算する

        Returns
        -------
        passed_length: int
            アリが通ったルートの長さの合計
        """
        passed_length = 0
        for i in range(self.params.num_node-1):
            passed_length += self.graph.length_edge[
                self.visited_routes[i]][
                self.visited_routes[i+1]
            ]
        return passed_length
