# AI-Based Route Optimization using A* and Graph Algorithms

## Project Overview
This project is an intelligent route planning system built in Python. It utilizes fundamental graph theory and advanced heuristic search algorithms to find the most optimal path between interconnected nodes (cities). The system compares three distinct traversal algorithms—Breadth-First Search (BFS), Depth-First Search (DFS), and A* (A-Star) Search—evaluating them based on execution time, path cost, and optimality.

## Why is this Important? (Real-World Application)
Route optimization is a cornerstone of modern computer science and artificial intelligence. Finding the shortest, fastest, or cheapest path between two points is critical for:
* **Logistics & Supply Chain:** Companies like Amazon and FedEx use these algorithms to route delivery trucks, saving millions in fuel costs and reducing carbon emissions.
* **Navigation Systems:** Google Maps and GPS devices rely on variations of A* and Dijkstra's algorithms to provide real-time turn-by-turn directions.
* **Autonomous Vehicles:** Self-driving cars map their immediate environment as a graph to navigate around obstacles safely.
* **Network Routing:** Data packets traveling across the internet rely on shortest-path algorithms to reach their destination quickly without bottlenecking servers.

---

## Theoretical Background

This project models the map as a **Graph**. 
* **Nodes (Vertices):** Represent the cities (e.g., Arad, Bucharest).
* **Edges:** Represent the roads connecting the cities.
* **Weights:** Represent the distance or cost to travel across an edge.

### 1. Breadth-First Search (BFS)
* **Classification:** Uninformed (Blind) Search.
* **How it works:** BFS explores the graph level by level. It checks all immediate neighbors of the starting city before moving deeper into the map. 
* **Pros & Cons:** BFS guarantees finding a path to the goal. However, it ignores edge weights (distances). Therefore, it will find the path with the *fewest number of stops*, which is rarely the shortest distance in a real-world weighted map.

### 2. Depth-First Search (DFS)
* **Classification:** Uninformed (Blind) Search.
* **How it works:** DFS dives as deep as possible down a single path until it hits a dead end, then it backtracks and tries the next path. 
* **Pros & Cons:** DFS uses less memory than BFS, but it is notoriously bad for route optimization. It will easily get stuck exploring long, inefficient detours and is not guaranteed to find the optimal path.

### 3. A* Search Algorithm (The Optimal Solution)
* **Classification:** Informed (Heuristic) Search.
* **How it works:** A* is the gold standard for pathfinding. It calculates a mathematical cost for every potential next step using the formula:
  
  $$f(n) = g(n) + h(n)$$

  * **$g(n)$ (Actual Cost):** The exact distance traveled so far from the starting node to node $n$.
  * **$h(n)$ (Heuristic Cost):** An educated guess (estimate) of the distance from node $n$ to the final goal (e.g., a straight-line distance).
  * **$f(n)$ (Total Cost):** The node with the lowest $f(n)$ is always explored next.
* **Pros & Cons:** Because A* considers both the distance already traveled and the estimated distance remaining, it is incredibly efficient and mathematically guaranteed to find the shortest possible path, provided the heuristic never overestimates the actual distance.

---

## How the Project Works (Under the Hood)

1. **Graph Construction (`graph_manager.py`):** The system uses `NetworkX` to build a mathematical model of the cities. It registers the exact distance between connected cities and stores the heuristic data (straight-line distance to the target).
2. **Algorithm Execution (`algorithms.py`):** The `RouteOptimizer` runs BFS, DFS, and A* simultaneously. It measures the execution time (in milliseconds) and calculates the total travel cost for the paths each algorithm discovers.
3. **Visualization (`visualizer.py`):** Using `Matplotlib`, the system generates an interactive, graphical representation of the map. It highlights the optimal path discovered by the A* algorithm, allowing users to visually verify the AI's decision-making process.

---

## Project Structure

```text
route_optimizer/
│
├── src/
│   ├── __init__.py
│   ├── graph_manager.py     # Graph creation and node/edge data
│   ├── algorithms.py        # BFS, DFS, and A* logic
│   └── visualizer.py        # Matplotlib rendering and UI
│
├── tests/
│   ├── __init__.py
│   └── test_algorithms.py   # Pytest unit tests for algorithm verification
│
├── main.py                  # Entry point script and performance comparison
└── requirements.txt         # Dependencies (NetworkX, Matplotlib, Pytest)