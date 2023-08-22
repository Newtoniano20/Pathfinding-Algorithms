from .Algorithm import Algorithm

class AStar(Algorithm):
    def __init__(self, goal, origin):
        self.frontier = []
        self.goal = goal
        self.origin = origin
        self.goal_weight = 1.1
        self.origin_weight = 1
        self.hv = dict()

    def h(self, state):
        if state in self.hv.keys():
            return self.hv[state]
        else:
            r, c = state
            g_r, g_c = self.goal
            o_r, o_c = self.origin
            self.hv[state] = self.goal_weight*(abs(r-g_r) + abs(c - g_c)) + self.origin_weight*(abs(r-o_r) + abs(c - o_c))
            return self.hv[state]
    
    def remove(self):
        """
        Gives back the best node to follow using A* Algorithm
        """
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            best_h = self.h(node.state)
            for n in self.frontier:
                nh = self.h(n.state)
                if nh < best_h:
                    best_h = nh
                    node = n
            self.frontier.remove(node)
            return node
