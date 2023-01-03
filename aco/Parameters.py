class Parameters:
    """
    Attributes
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

    def __init__(self, num_ant, num_node, q, alpha, beta, rou,
                 max_iteration, min_tau, max_tau, border_unchanged,
                 start_node):
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
        self.num_ant = num_ant
        self.num_node = num_node
        self.q = q
        self.alpha = alpha
        self.beta = beta
        self.rou = rou
        self.max_iteration = max_iteration
        self.min_tau = min_tau
        self.max_tau = max_tau
        self.border_unchanged = border_unchanged
        self.start_node = start_node
