import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer:
    """Visualizes the graph and highlights specific paths."""
    
    def __init__(self, graph_manager):
        self.graph = graph_manager.get_graph()
        # Spring layout calculates positions for nodes to make the graph look nice
        self.pos = nx.spring_layout(self.graph, seed=42) 

    def draw(self, path=None, algorithm_name="Graph"):
        plt.figure(figsize=(8, 6))

        # 1. Draw all nodes and edges
        nx.draw(self.graph, self.pos, with_labels=True, node_color='lightblue',
                node_size=1500, font_size=10, font_weight='bold', edge_color='gray')

        # 2. Draw edge weights (distances)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=edge_labels)

        # 3. Highlight the found path (if any)
        if path:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_nodes(self.graph, self.pos, nodelist=path, node_color='lightgreen', node_size=1500)
            nx.draw_networkx_edges(self.graph, self.pos, edgelist=path_edges, edge_color='red', width=3)

        plt.title(f"Route Optimization - {algorithm_name}")
        plt.axis('off') # Hide axes
        plt.show()