from aco.solver import Solver

solver = Solver(num_ant=30, num_node=50, q=100, alpha=3, beta=5, rou=0.9,
                max_iteration=300, min_tau=9, max_tau=3000,
                border_unchanged=30, start_node=1,
                path="./data/qiita_data.json")
