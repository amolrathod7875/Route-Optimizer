import time
from src.graph_manager import GraphManager
from src.algorithms import RouteOptimizer
from src.visualizer import GraphVisualizer

def main():
    # 1. Initialize Graph
    gm = GraphManager()

    # Let's create a simplified Indian Map example
    # Goal is to reach 'Bengaluru'
    gm.add_city('Mumbai', heuristic_value=366)
    gm.add_city('Surat', heuristic_value=374)
    gm.add_city('Pune', heuristic_value=253)
    gm.add_city('Nashik', heuristic_value=329)
    gm.add_city('Kolhapur', heuristic_value=176)
    gm.add_city('Solapur', heuristic_value=193)
    gm.add_city('Bengaluru', heuristic_value=0)

    # Add edges (routes and their distances/costs)
    gm.add_route('Mumbai', 'Surat', 75)
    gm.add_route('Mumbai', 'Pune', 140)
    gm.add_route('Mumbai', 'Nashik', 118)
    gm.add_route('Pune', 'Kolhapur', 99)
    gm.add_route('Pune', 'Solapur', 80)
    gm.add_route('Kolhapur', 'Bengaluru', 211)
    gm.add_route('Solapur', 'Bengaluru', 240) # Custom test path for A* vs DFS

    # 2. Setup Optimizer and Visualizer
    optimizer = RouteOptimizer(gm)
    visualizer = GraphVisualizer(gm)

    start_city = 'Mumbai'
    goal_city = 'Bengaluru'

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