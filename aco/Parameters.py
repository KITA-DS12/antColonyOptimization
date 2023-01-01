class Parameters:
    def __init__(self, num_ant, num_vertex, q, alpha, beta, rou,
                 max_iteration, initial_vertex, min_tau, max_tau):
        self.num_ant = num_ant
        self.num_vertex = num_vertex
        self.q = q
        self.alpha = alpha
        self.beta = beta
        self.rou = rou
        self.max_iteration = max_iteration
        self.initial_vartex = initial_vertex
        self.min_tau = min_tau
        self.max_tau = max_tau
