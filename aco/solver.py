from aco.parameters import Parameters
from aco.graph import Graph
from aco.colony import Colony


class Solver:
    """
    ACOの管理・実行を行う

    Attributes
    ----------
    params: Parameters
        ACOを設定するすべてのパラメータを保存する
    graph: Graph
        ノードの座標やエッジの距離，フェロモン量などを保存する
    colony: Colony
        Ant全体を管理し，パスの構築やフェロモンの分泌，初期化等を行う
    best_ant: Ant
        全サイクルで最も良い結果を出したアリを保持する
    good_ant: Ant
        最新のサイクルで最も良い結果を出したアリを保持する
    counter_unchanged: int
        best_antが更新されていない連続サイクル数をカウントする
    """

    def __init__(self, num_ant, num_node, q, alpha, beta, rou,
                 max_iteration, min_tau, max_tau, border_unchanged,
                 start_node, path):
        """
        Parameters
        ----------
        num_ant: int
            アリの数
        num_node: int
            ノードの数
        q: int
            分泌するフェロモン量に影響するパラメータ
        alpha: float
            フェロモンの重みパラメータ
        beta: float
            ヒューリスティック値の重みパラメータ
        rou: float
            蒸発率
        max_iteration: int
            サイクルの実行回数
        min_tau: int
            フェロモン量の下限
        max_tau: int
            フェロモン量の上限
        border_unchanged: int
            フェロモンをリセットするサイクル数
        start_node: int
            探索を始めるノードのインデックス
        """
        self.params = Parameters(num_ant, num_node, q, alpha, beta, rou,
                                 max_iteration, min_tau, max_tau,
                                 border_unchanged, start_node)
        self.graph = Graph(self.params, path)
        self.colony = Colony(self.params, self.graph)
        self.best_ant = None
        self.good_ant = None
        self.counter_unchanged = 0

    def run_aco(self):
        """
        {max_iteration}回，ACOのサイクルを実行し，解をbest_antに格納する
        """
        for _ in range(self.params.max_iteration):
            self.__run_cycle_aco()

            if (self.best_ant is None) or (self.good_ant > self.best_ant):
                self.best_ant = self.good_ant
            else:
                self.counter_unchanged += 1

            """
            {border_unchanged}サイクル間，
            best_antが更新されなかったらフェロモンをリセットする
            """
            if self.counter_unchanged > self.params.border_unchanged:
                self.graph.reset_pheromones()
                self.counter_unchanged = 0

    def __run_cycle_aco(self):
        """
        サイクルの一連処理を行う
        """
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
