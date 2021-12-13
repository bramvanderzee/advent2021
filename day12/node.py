class Node:
    char, cost = None, None
    unique = False
    adj = None

    def __init__(self, char):
        self.char = char
        self.adj = []
    
    def add_cost(self, cost):
        self.cost = cost
        
    def add_adj(self, node):
        if not node in self.adj:
            self.adj.append(node)
    
    def __eq__(self, other):
        return self.char == other.char

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self):
        return str([self.char, self.cost, [n.char for n in self.adj]])

    def __repr__(self):
        return self.char