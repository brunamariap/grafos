from utils import read_json, key_converter
from draw_interface import draw_interface

def search_with_dijkstra():
    from dijkstra import GraphDijkstra

    path = "graph1.json"
    graph = read_json(path)
    graph = key_converter(graph) 
    print(graph)

    start_node = 1
    end_node = 3

    graph_object = GraphDijkstra(graph)
    path, shortest_distance = graph_object.dijkstra(start_node, end_node)
    if shortest_distance:
        print(f"Menor distância de {start_node} para {end_node}: {shortest_distance}")

    draw_interface([node for node in graph.keys()], graph, path)

if __name__ == "__main__":
    search_with_dijkstra()