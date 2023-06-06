import sys

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

        print("\t"+"\t".join(self.nodes))
        for i in range(len(adj_mat)):
            nums = "\t".join(adj_mat[i])
            print(f"{self.nodes[i]}\t{nums}")

if __name__ == "__main__":
    graph = Graph(
        ["A","B","C","D","E"],
        [
            {"source":"A","target":"B","weight":5},
            {"source":"A","target":"C","weight":2},
            {"source":"B","target":"D","weight":4},
            {"source":"C","target":"D","weight":1},
            {"source":"C","target":"E","weight":3},
            {"source":"D","target":"E","weight":6},
            {"source":"E","target":"A","weight":2}
        ]
    )
    
    graph.adj_calc()