from .Algorithm import Algorithm

class Greedy(Algorithm):
    def __init__(self, goal, *args, **kwargs):
        self.frontier = []
        self.goal = goal
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
            self.hv[node] = abs(r-g_r) + abs(c - g_c)
            return self.hv[node]
            
    def remove(self):
        """
        Gives back the best node to follow using Greedy Breadth First Algorithm
        """
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = min(self.frontier, key=self.hv.get)
            self.frontier.remove(node)
            return node
