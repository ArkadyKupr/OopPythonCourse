from graph_task.graph import Graph

# задаем граф двумерным списком
user_graph = [[100, 1, 0, 0, 0, 0, 0],
              [1, 0, 1, 1, 1, 1, 0],
              [0, 1, 0, 0, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 1, 0, 1],
              [0, 0, 1, 0, 0, 1, 0]]

graph = Graph(user_graph)
print(graph)
print()

print("Обход в ширину")
print(graph.breadth_first_search())
print()

print("Обход в глубину без рекурсии")
print(graph.width_first_search())
print()

print("Обход в глубину с рекурсией")
print(graph.width_first_search_recursive())
