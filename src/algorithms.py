import heapq
from collections import deque

class RouteOptimizer:
    """Implements various search algorithms to find paths in a GraphManager."""
    
    def __init__(self, graph_manager):
        self.gm = graph_manager
        self.graph = graph_manager.get_graph()

    def bfs(self, start, goal):
        """Breadth-First Search: Explores neighbor nodes first."""
        queue = deque([(start, [start], 0)]) # (current_node, path, total_cost)
        visited = set()

        while queue:
            node, path, cost = queue.popleft()
            
            if node == goal:
                return path, cost
                
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.neighbors(node):
                    if neighbor not in visited:
                        edge_weight = self.graph[node][neighbor].get('weight', 1)
                        queue.append((neighbor, path + [neighbor], cost + edge_weight))
        
        return None, float('inf')

    def dfs(self, start, goal):
        """Depth-First Search: Explores as far as possible along each branch."""
        stack = [(start, [start], 0)]
        visited = set()

        while stack:
            node, path, cost = stack.pop() # LIFO
            
            if node == goal:
                return path, cost
                
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.neighbors(node):
                    if neighbor not in visited:
                        edge_weight = self.graph[node][neighbor].get('weight', 1)
                        stack.append((neighbor, path + [neighbor], cost + edge_weight))
                        
        return None, float('inf')

    def a_star(self, start, goal):
        """A* Search: Uses cost so far + heuristic estimate to find optimal path."""
        # Priority queue stores tuples of: (f_score, current_cost, current_node, path)
        # f_score = g_cost (actual distance so far) + h_cost (heuristic estimate to goal)
        open_set = [(self.gm.get_heuristic(start), 0, start, [start])]
        visited = set()

        while open_set:
            _, current_cost, current_node, path = heapq.heappop(open_set)

            if current_node == goal:
                return path, current_cost

            if current_node in visited:
                continue
                
            visited.add(current_node)

            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    edge_weight = self.graph[current_node][neighbor].get('weight', 1)
                    new_cost = current_cost + edge_weight
                    f_score = new_cost + self.gm.get_heuristic(neighbor)
                    
                    heapq.heappush(open_set, (f_score, new_cost, neighbor, path + [neighbor]))
                    
        return None, float('inf')