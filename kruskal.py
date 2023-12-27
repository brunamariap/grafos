""" 
o objetivo principal do algoritmo de Kruskal é encontrar uma MST de um grafo ponderado, garantindo a conectividade de todos os vértices com o menor custo possível.
"""

class GraphKruskal:

    def __init__(self, graph):
        self.graph = graph

    # Método para encontrar o conjunto pai de um elemento em uma árvore.
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Método para unir dois subconjuntos na árvore.
    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        
        # Une os conjuntos
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            # Escolhe 1 para ser filho de um dos conjuntos
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                edges.append((u, v, self.graph[u][v]))

        edges = sorted(edges, key=lambda x: x[2]) # Ordena as arestas
        parent = {vertex: vertex for vertex in self.graph}
        rank = {vertex: 0 for vertex in self.graph}
        minimum_spanning_tree = []

        # Itera sobre as arestas ordenadas.
        for edge in edges:
            u, v, weight = edge
            u_parent = self.find(parent, u)
            v_parent = self.find(parent, v)
            
            # Verifica se a inclusão da aresta forma um ciclo na árvore.
            if u_parent != v_parent:
                minimum_spanning_tree.append((u, v, weight))
                self.union(parent, rank, u_parent, v_parent)

        return minimum_spanning_tree
    
from utils import read_json, key_converter
import networkx as nx
import matplotlib.pyplot as plt

graph = read_json('graph1.json')
graph = key_converter(graph)

grafo = GraphKruskal(graph)
minimum_spanning_tree = grafo.kruskal()

print("Árvore Geradora Mínima:")
print(minimum_spanning_tree)

G = nx.Graph()

G.add_nodes_from([node for node in graph.keys()])
position = nx.spring_layout(G) 

edges = []
edges_labels = {}

# for external_key, values in graph.items():
#     for internal_key, distance in values.items():
#         if (external_key, internal_key) in edges or (internal_key, external_key) in edges:
#             continue
#         edges.append((external_key, internal_key))
#         edges_labels[(external_key, internal_key)] = distance

new_edges = [(edge[0], edge[1]) for edge in minimum_spanning_tree]
edges_labels = {(edge[0], edge[1]):edge[2] for edge in minimum_spanning_tree}

# G.add_edges_from(edges)
nx.draw(G, position, with_labels=True,
            node_color='lightblue', font_weight='bold')

nx.draw_networkx_edges(
        G, position, edgelist=new_edges, edge_color='red', width=3)

nx.draw_networkx_edge_labels(G, position, edge_labels=edges_labels)

plt.title('Grafo')
plt.show()