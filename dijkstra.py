class GraphDijkstra:

    def __init__(self, graph: dict):
        self.graph = graph
        self.distances = {node: float('inf') for node in graph}
        self.predecessors = {node: None for node in graph}
    
    def min_distance(self, visited, distances):
        min_distance = float('inf')
        current_node = None
        
        for node in self.graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node
        
        if current_node:
            return current_node
        
    def get_path(self, start_node, end_node):
        path = []
        current_node = end_node
        while current_node is not None:
            path.insert(0, current_node)
            current_node = self.predecessors[current_node]
        print(path)
        return path
    
    def dijkstra(self, start_node, end_node):
        if start_node in self.graph.keys() and end_node in self.graph.keys():
            distances = self.distances.copy()
            distances[start_node] = 0
            visited = set()

            # Enquanto existirem nós não visitados
            while len(visited) < len(self.graph):
                current_node = self.min_distance(visited, distances)
                visited.add(current_node)
                if current_node == end_node:
                    break

                for neighbor, weight in self.graph[current_node].items():
                    distance = distances[current_node] + weight
                    # Distância do atual é menor que a do vizinho
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        # Armazena o predecessor do vizinho que no caso é o atual
                        self.predecessors[neighbor] = current_node

            print(distances)
            print(self.predecessors)
            path = self.get_path(start_node, end_node)
            return path, distances[end_node]

        print("Pelo menos 1 dos vértices informados não existe no grafo")
        return False
