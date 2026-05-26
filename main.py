import time
from src.graph_manager import GraphManager
from src.algorithms import RouteOptimizer
from src.visualizer import GraphVisualizer

def main():
    # 1. Initialize Graph
    gm = GraphManager()

    # Let's create a simplified Romanian Map example (Classic AI graph problem)
    # Goal is to reach 'Bucharest'
    gm.add_city('Arad', heuristic_value=366)
    gm.add_city('Zerind', heuristic_value=374)
    gm.add_city('Sibiu', heuristic_value=253)
    gm.add_city('Timisoara', heuristic_value=329)
    gm.add_city('Fagaras', heuristic_value=176)
    gm.add_city('Rimnicu Vilcea', heuristic_value=193)
    gm.add_city('Bucharest', heuristic_value=0)

    # Add edges (routes and their distances/costs)
    gm.add_route('Arad', 'Zerind', 75)
    gm.add_route('Arad', 'Sibiu', 140)
    gm.add_route('Arad', 'Timisoara', 118)
    gm.add_route('Sibiu', 'Fagaras', 99)
    gm.add_route('Sibiu', 'Rimnicu Vilcea', 80)
    gm.add_route('Fagaras', 'Bucharest', 211)
    gm.add_route('Rimnicu Vilcea', 'Bucharest', 240) # Changed from standard map to test A* vs DFS

    # 2. Setup Optimizer and Visualizer
    optimizer = RouteOptimizer(gm)
    visualizer = GraphVisualizer(gm)

    start_city = 'Arad'
    goal_city = 'Bucharest'

    print(f"--- Route Optimization: {start_city} to {goal_city} ---\n")

    # 3. Run and Compare Algorithms
    algorithms = {
        "BFS": optimizer.bfs,
        "DFS": optimizer.dfs,
        "A*": optimizer.a_star
    }

    results = {}

    for name, func in algorithms.items():
        start_time = time.perf_counter()
        path, cost = func(start_city, goal_city)
        end_time = time.perf_counter()
        
        execution_time = (end_time - start_time) * 1000 # Convert to milliseconds
        results[name] = {"path": path, "cost": cost, "time": execution_time}
        
        print(f"[{name}] Path: {' -> '.join(path)}")
        print(f"[{name}] Total Cost: {cost}")
        print(f"[{name}] Time Taken: {execution_time:.4f} ms\n")

    # 4. Visualize the A* optimal result
    best_algo = "A*"
    best_path = results[best_algo]["path"]
    
    print("Close the popup window to end the program.")
    visualizer.draw(path=best_path, algorithm_name=f"{best_algo} (Cost: {results[best_algo]['cost']})")

if __name__ == "__main__":
    main()