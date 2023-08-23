from .Algorithm import Algorithm

class AStar(Algorithm):
    def __init__(self, goal, origin):
        self.frontier = []
        self.goal = goal
        self.origin = origin
        self.goal_weight = 1
        self.origin_weight = 1
        self.hv = dict()

    def add(self, node):
        self.h(node)
        self.frontier.append(node)

    def h(self, node):
        if node in self.hv.keys():
            return self.hv[node]
        else:
            r, c = node.state
            g_r, g_c = self.goal
            o_r, o_c = self.origin
            self.hv[node] = self.goal_weight*(abs(r-g_r) + abs(c - g_c)) + self.origin_weight*(abs(r-o_r) + abs(c - o_c))
            return self.hv[node]
    
    def remove(self):
        """
        Gives back the best node to follow using A* Algorithm
        """
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = min(self.frontier, key=self.hv.get)
            self.frontier.remove(node)
            return node
