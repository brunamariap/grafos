""" 
Ele é utilizado para encontrar a árvore geradora mínima em um grafo ponderado, ou seja, um subconjunto de arestas que conecta todos os vértices do grafo com o menor custo total possível, sem formar ciclos.
é preciso escolher um grafo para começar
"""

class GraphPrim:
    def __init__(self, graph_dict):
        self.graph = graph_dict

    def prim(self, ):
        minimum_spanning_tree = {}  
        visited = set() 

        start_vertex = list(self.graph.keys())[0]  # Escolhe o primeiro vértice como inicial
        visited.add(start_vertex) 

        while len(visited) < len(self.graph):  # Enquanto houver vértices não visitados no grafo
            min_weight = float('inf') 
            min_edge = None

            # Percorre os vértices já visitados
            for node in visited:
                # print('node', node)
                # Itera sobre os vizinhos do vértice atual
                for neighbor, weight in self.graph[node].items():
                    # Verifica se o vizinho não está visitado e se seu peso é menor que o mínimo atual
                    if neighbor not in visited and weight < min_weight:
                        min_weight = weight 
                        min_edge = (node, neighbor) 

            # Se uma aresta mínima foi encontrada
            if min_edge:
                minimum_spanning_tree[min_edge] = min_weight  # Adiciona a aresta mínima à árvore geradora mínima
                visited.add(min_edge[1])  # Adiciona o vértice conectado à árvore aos visitados

        return minimum_spanning_tree  # Retorna a árvore geradora mínima

from utils import read_json, key_converter
import networkx as nx
import matplotlib.pyplot as plt

json_data = read_json('graph1.json')
formatted_graph = key_converter(json_data)

g = GraphPrim(formatted_graph)
minimum_spanning_tree = g.prim()

print("Árvore Geradora Mínima:")
print(minimum_spanning_tree)


G = nx.Graph()

G.add_nodes_from([node for node in formatted_graph.keys()])
position = nx.spring_layout(G)  # Posicionamento dos vértices

edges = []
edges_labels = {}

# for external_key, values in formatted_graph.items():
#     for internal_key, distance in values.items():
#         if (external_key, internal_key) in edges or (internal_key, external_key) in edges:
#             continue
#         edges.append((external_key, internal_key))
#         edges_labels[(external_key, internal_key)] = distance

new_edges = [edge for edge in minimum_spanning_tree.keys()]
# edges_labels = {edge:distance for edge in minimum_spanning_tree.items()}

# G.add_edges_from(edges)
nx.draw(G, position, with_labels=True,
            node_color='lightblue', font_weight='bold')

nx.draw_networkx_edges(
        G, position, edgelist=new_edges, edge_color='red', width=3)

nx.draw_networkx_edge_labels(G, position, edge_labels=minimum_spanning_tree)

plt.title('Grafo')
plt.show()
