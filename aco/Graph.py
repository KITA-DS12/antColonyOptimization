class Graph:
    """
    ノードやエッジ，フェロモンなどを管理する

    Attributes
    ----------
    params: Parameters
        ACOを設定するすべてのパラメータを保存する
    coordinates: list of tuple of float
        ノードの座標を格納する
    length_edge: list of int
        エッジの長さを格納する
    pheromone_edge: list of int
        現在蓄積されているエッジのフェロモン量を格納する
    next_pheromone_edge: list of int
        最新のサイクルで分泌されたフェロモン量を格納する
    heuristics_edge: list of int
        エッジのヒューリスティック値を格納する
    """

    def __init__(self, parameters, path):
        """
        Parameters
        ----------
        parameters: Parameters
            ACOを設定するすべてのパラメータを保存する
        """
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
        self.__prepare_graph(path)

    def __prepare_graph(self, path):
        """
        受け取ったグラフ構造の情報を読み取る
        """
        pass

    def reset_pheromones(self):
        """
        エッジに蓄積したフェロモンをすべてリセットする
        """
        for i in range(self.params.num_node):
            for j in range(self.params.num_node):
                if i < j:
                    self.pheromone_edge[i][j] = \
                        self.params.q / self.length_edge[i][j]
                    self.pheromone_edge[j][i] = \
                        self.params.q / self.length_edge[j][i]
