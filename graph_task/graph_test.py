from graph_task.graph import Graph

graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "A")
graph.add_edge("A", "B")
graph.add_edge("C", "B")
graph.print_graph()
