import sys
from queue import Queue

M = sys.maxsize

class Graph:

    def __init__(self,nodes, edges):
        self.nodes = nodes
        self.edges = edges


    def adj_calc(self):
        adj_mat =[[" "]*len(self.nodes) for _ in range(len(self.nodes))]
        for i in range(len(adj_mat)):
            relevant_edges = [j for j in self.edges if j["source"] == self.nodes[i]]
            for k in relevant_edges:
                indx = self.nodes.index(k["target"])
                adj_mat[i][indx] = str(k["weight"])
            adj_mat[i] = list(map(lambda x: x.replace(" ", "0"), adj_mat[i]))

        self.adj = adj_mat
        
    def __str__(self):   
        print("\t"+"\t".join(self.nodes))
        for i in range(len(self.adj)):
            nums = "\t".join(self.adj[i])
            print(f"{self.nodes[i]}\t{nums}")
        return ""

    def dfs(self, target):
        start = self.nodes[0]
        relevant_edges = {i:j for i in self.nodes for j in self.edges if j["source"] == i}
        print(relevant_edges)

    def bfs(self, target):
        n = len(self.nodes)
        nodes = self.nodes
        search = Queue(n)
        for i in range(n):
            print(search.get())


if __name__ == "__main__":
    graph = Graph(
        ["A", "B", "C", "D", "E"],
    [
        {"source": "A", "target": "B", "weight": 5},
        {"source": "B", "target": "A", "weight": 5},
        {"source": "A", "target": "C", "weight": 2},
        {"source": "C", "target": "A", "weight": 2},
        {"source": "B", "target": "D", "weight": 4},
        {"source": "D", "target": "B", "weight": 4},
        {"source": "C", "target": "D", "weight": 1},
        {"source": "D", "target": "C", "weight": 1},
        {"source": "C", "target": "E", "weight": 3},
        {"source": "E", "target": "C", "weight": 3},
        {"source": "D", "target": "E", "weight": 6},
        {"source": "E", "target": "D", "weight": 6},
        {"source": "E", "target": "A", "weight": 2},
        {"source": "A", "target": "E", "weight": 2},
        {"source": "B", "target": "A", "weight": 5},
        {"source": "C", "target": "A", "weight": 2},
        {"source": "D", "target": "B", "weight": 4},
        {"source": "D", "target": "C", "weight": 1},
        {"source": "E", "target": "C", "weight": 3},
        {"source": "E", "target": "D", "weight": 6},
        {"source": "A", "target": "E", "weight": 2}
    ]
)


    graph.adj_calc()
    print(graph)

    graph.bfs("A")
