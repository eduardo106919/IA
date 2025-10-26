
from Graph import Graph

class Buckets:
    """
    A class representing two buckets with diferent capacities

    Attributes:
        g (Graph): Graph that represents the possible operations
        start (tuple): starting contents of each bucket
        goal (tuple): contents that each bucket should have
        bucket1_cap (int): capacity of the first bucket
        bucket2_cap (int): capacity of the second bucket
    """

    def __init__(self, start=(0,0), goal=(0,0), bucket1_cap=0, bucket2_cap=0):
        self.g = None
        self.start = start
        self.goal = goal
        self.bucket1_cap = bucket1_cap
        self.bucket2_cap = bucket2_cap

    def create_graph(self):
        self.g = Graph(directed=True)

        # states added to the graph
        visited : set = set()

        # states to expand
        open_list : list = list()
        open_list.append(self.start)

        while len(open_list) != 0:
            current = open_list.pop(0)
            expansion = self.expand_state(current)

            for e in expansion:
                if e not in visited:
                    visited.add(e)
                    self.g.add_edge(str(current), str(e), 1)
                    open_list.append(e)

        return self.g


    def expand_state(self, state):
        expansion = list()

        if state[0] > 0:
            expansion.append(self.empty_bucket1(state))
        if state[1] > 0:
            expansion.append(self.empty_bucket2(state))
        if state[0] < self.bucket1_cap:
            expansion.append(self.fill_bucket1(state))
        if state[1] < self.bucket2_cap:
            expansion.append(self.fill_bucket2(state))
        if state[0] > 0 and state[1] < self.bucket2_cap:
            expansion.append(self.tranfer_1_2(state))
        if state[1] > 0 and state[0] < self.bucket1_cap:
            expansion.append(self.tranfer_2_1(state))

        return expansion

    def empty_bucket1(self, state):
        return 0, state[1]

    def empty_bucket2(self, state):
        return state[0], 0

    def fill_bucket1(self, state):
        return self.bucket1_cap, state[1]

    def fill_bucket2(self, state):
        return state[0], self.bucket2_cap

    def tranfer_1_2(self, state):
        first = state[0]
        second = state[1]
        second += first

        if second > self.bucket2_cap:
            temp = second - self.bucket2_cap
            first = temp
            second = self.bucket2_cap
        else:
            first = 0

        return first, second

    def tranfer_2_1(self, state):
        first = state[0]
        second = state[1]
        first += second

        if first > self.bucket1_cap:
            temp = first - self.bucket1_cap
            second = temp
            first = self.bucket1_cap
        else:
            second = 0

        return first, second

    def get_graph(self):
        return self.g

    def get_start(self):
        return self.start

    def get_goal(self):
        return self.goal

    def set_start(self, start : tuple):
        self.start = start

    def set_goal(self, goal : tuple):
        self.goal = goal

