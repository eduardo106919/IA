
import math
import queue

import networkx as nx
import matplotlib.pyplot as plt


class Graph:


    def __init__(self, directed = False):
        # dictionary that holds lists of pairs (node, weight)
        self.edges = dict()
        self.directed = directed
        # dictionary that holds the heuristic values for each node
        self.heuristics = dict()


    def __str__(self):
        out = ""
        for (current, l) in self.edges.items():
            out = out + "[" + str(self.heuristics[current]) + ", " + str(current) + "] -> "
            for (node, weight) in l:
                out = out + "(" + node + ", " + str(weight) + ") -> "
            out = out + "X\n"
        return out


    def get_nodes(self):
        ns = set()
        for n in self.edges.keys():
            ns.add(n)
        return ns


    def add_edge(self, src, dest, weight=0):
        # src is a new node
        if src not in self.edges:
            self.edges[src] = []
        # dest is a new node
        if dest not in self.edges:
            self.edges[dest] = []

        self.edges[src].append((dest, weight))
        # graph has no direction
        if not self.directed:
            self.edges[dest].append((src, weight))


    def get_edge_cost(self, src, dest):
        for (node, weight) in self.edges[src]:
            if node == dest:
                return weight
        return math.inf


    def get_neighbours(self, node):
        return self.edges[node]


    def get_path_cost(self, path):
        cost = 0
        i = 0
        while i + 1 < len(path):
            c = self.get_edge_cost(path[i], path[i + 1])
            # invalid path
            if c is math.inf:
                return math.inf

            cost = cost + c
            i = i + 1

        return cost


    def add_heuristic(self, node, h):
        if node in self.edges:
            self.heuristics[node] = h


    def draw(self):
        g = nx.Graph()
        for node in self.edges.keys():
            g.add_node(node)
            for (neighbour, w) in self.edges[node]:
                g.add_edge(node, neighbour, weight=w)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()


    def depth_first_search(self, src, dest, path=list(), visited=set()):
        visited.add(src)
        path.append(src)

        if src == dest:
            return True

        for (node, w) in self.edges[src]:
            # node not visited
            if node not in visited:
                if self.depth_first_search(node, dest, path, visited):
                    return True

        path.pop()
        return False


    def breadth_first_search(self, src, dest, path=list(), visited=set()):
        visited.add(src)

        if src == dest:
            return True

        found = False

        # queue for nodes to visit
        q = queue.Queue()
        q.put(src)

        # dictionary to reconstruct the path
        parents = dict()
        parents[src] = None

        while not q.empty() and not found:
            current = q.get()

            for (node, w) in self.edges[current]:
                # node not visited
                if node not in visited:
                    visited.add(node)
                    parents[node] = current
                    if node == dest:
                        found = True
                        break
                    q.put(node)

        # if dest was found, reconstruct the path
        if found:
            current = dest
            while parents[current] is not None:
                path.append(current)
                current = parents[current]

            path.append(src)
            path.reverse()

        return found


    def greedy_search(self, src, dest, path=list(), visited=set()):
        visited.add(src)

        if src == dest:
            path.append(src)
            return True

        # list of nodes that are still valid to keep searching
        open_nodes = list()
        open_nodes.append((self.heuristics[src], src))

        # dictionary to reconstruct the path
        parents = dict()
        parents[src] = None
        found = False

        while len(open_nodes) > 0 and not found:
            h, current = min(open_nodes)
            open_nodes.remove((h, current))

            if current == dest:
                found = True
                break

            for node, _ in self.edges[current]:
                if node not in visited:
                    if node == dest:
                        parents[node] = current
                        found = True
                        break

                    visited.add(node)
                    parents[node] = current
                    open_nodes.append((self.heuristics[node], node))

        # destiny was found, reconstruct the path
        if found:
            current = dest
            while current is not None:
                path.append(current)
                current = parents[current]
            path.reverse()

        # destiny was not found
        return found


    def a_star_search(self, src, dest, path=list(), visited=set()):
        visited.add(src)

        if src == dest:
            return True

        costs = dict()
        costs[src] = 0

        # list of nodes that are still valid to keep searching
        open_nodes = list()
        open_nodes.append((self.heuristics[src], src))

        # dictionary to reconstruct the path
        parents = dict()
        parents[src] = None
        found = False

        while len(open_nodes) > 0 and not found:
            h, current = min(open_nodes)
            open_nodes.remove((h, current))

            if current == dest:
                found = True
                break

            for node, w in self.edges[current]:
                if node == dest:
                    parents[node] = current
                    found = True
                    break

                temp = costs[current] + w
                if node not in costs or temp < costs[node]:
                    visited.add(node)
                    costs[node] = temp
                    parents[node] = current
                    open_nodes.append((self.heuristics[node] + temp, node))

        if found:
            current = dest
            while current is not None:
                path.append(current)
                current = parents[current]
            path.reverse()

        return found

