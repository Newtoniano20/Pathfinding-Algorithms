from .Algorithm import Algorithm

class Greedy(Algorithm):
    def __init__(self, goal, *args, **kwargs):
        self.frontier = []
        self.goal = goal
        self.hv = dict()
    
    def h(self, state):
        # Uses Manhattan distance
        if state in self.hv.keys():
            return self.hv[state]
        else:
            r, c = state
            g_r, g_c = self.goal
            self.hv[state] = abs(r-g_r) + abs(c - g_c)
            return self.hv[state]
        
    def remove(self):
        """
        Gives back the best node to follow using Greedy Breadth First Algorithm
        """
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            best_h = self.h(self.frontier[0].state)
            for n in self.frontier:
                if self.h(n.state) < best_h:
                    best_h = self.h(n.state)
                    node = n
            self.frontier.remove(node)
            if self.frontier is None:
                self.frontier = []
            return node
