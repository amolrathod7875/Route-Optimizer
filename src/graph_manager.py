import networkx as nx

class GraphManager:
    """Manages the graph representation, edges, and heuristic data."""
    
    def __init__(self):
        self.graph = nx.Graph()
        self.heuristics = {}

    def add_city(self, name, heuristic_value=0):
        """Add a city with a heuristic value (estimated distance to goal)."""
        self.graph.add_node(name)
        self.heuristics[name] = heuristic_value

    def add_route(self, city1, city2, distance):
        """Add an edge representing a route between two cities."""
        self.graph.add_edge(city1, city2, weight=distance)

    def get_heuristic(self, city):
        return self.heuristics.get(city, 0)

    def get_graph(self):
        return self.graph