import pytest
from src.graph_manager import GraphManager
from src.algorithms import RouteOptimizer

@pytest.fixture
def setup_graph():
    """Fixture to create a standard graph before each test."""
    gm = GraphManager()
    
    gm.add_city('A', heuristic_value=10)
    gm.add_city('B', heuristic_value=5)
    gm.add_city('C', heuristic_value=2)
    gm.add_city('Goal', heuristic_value=0)
    
    gm.add_route('A', 'B', 2)
    gm.add_route('A', 'C', 4)
    gm.add_route('B', 'Goal', 8)  # Path A-B-Goal: Cost 10
    gm.add_route('C', 'Goal', 3)  # Path A-C-Goal: Cost 7 (Optimal)
    
    return RouteOptimizer(gm)

def test_bfs(setup_graph):
    path, cost = setup_graph.bfs('A', 'Goal')
    # BFS might find A->B->Goal first depending on edge retrieval order, but it must reach Goal.
    assert path[-1] == 'Goal'
    assert path[0] == 'A'

def test_dfs(setup_graph):
    path, cost = setup_graph.dfs('A', 'Goal')
    assert path[-1] == 'Goal'
    assert path[0] == 'A'

def test_a_star_optimal_path(setup_graph):
    path, cost = setup_graph.a_star('A', 'Goal')
    # A* MUST find the cheapest path (A -> C -> Goal, cost: 7)
    assert path == ['A', 'C', 'Goal']
    assert cost == 7