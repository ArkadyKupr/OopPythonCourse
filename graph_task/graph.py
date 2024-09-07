from queue import Queue


class Graph:
    def __init__(self, graph):
        if not isinstance(graph, list):
            raise TypeError(f"Тип {graph} не является list")

        for row in graph:
            if not isinstance(row, list):
                raise TypeError(f"Тип {row} не является list")

        # Проверка размерности и чтобы когда i=j элемент списка имел значение 0
        rows_quantity = len(graph)

        if rows_quantity == 0:
            raise ValueError(f"Граф не должен быть пустым")

        for row in graph:
            if len(row) != rows_quantity:
                raise IndexError(f"Количество столбцов в строке {row}: {len(row)}, "
                                 f"не равно заданному количеству строк {rows_quantity}")

        for i in range(rows_quantity):
            for j in range(rows_quantity):
                if i == j:
                    graph[i][j] = 0

        self.__graph = graph

    @property
    def vertex_quantity(self):
        return len(self.__graph)

    def __repr__(self):
        rows_list = ""

        for i in range(self.vertex_quantity):
            for j in range(self.vertex_quantity):
                rows_list += str(self.__graph[i][j])
                rows_list += " "

            rows_list += "\n"

        return rows_list

    # Обход в ширину
    def breadth_first_search(self):
        visited = [False] * self.vertex_quantity

        # Использование очереди
        vertexes_queue = Queue()

        for i in range(self.vertex_quantity):
            if not visited[i]:
                vertexes_queue.put(self.__graph[i])
                visited[i] = True

                while not vertexes_queue.empty():
                    vertex = vertexes_queue.get()
                    print(vertex)

                    for j in range(self.vertex_quantity):
                        if not visited[j] and vertex[j] == 1:
                            vertexes_queue.put(self.__graph[j])
                            visited[j] = True

                            break

        return visited

    # Обход в глубину без рекурсии
    def width_first_search(self):
        visited = [False] * self.vertex_quantity

        stack = []

        for i in range(self.vertex_quantity):
            if not visited[i]:
                stack.append(self.__graph[i])
                visited[i] = True

                while len(stack) > 0:
                    first_vertex = stack.pop()

                    for j in range(self.vertex_quantity):
                        if not visited[j] and first_vertex[j] == 1:
                            first_vertex.append(self.__graph[j])
                            visited[j] = True

        return visited

    # Обход в глубину c рекурсией
    def width_first_search_recursive(self):
        visited = [False] * self.vertex_quantity

        def visit(visited_recursive):
            for i in range(self.vertex_quantity):
                if not visited[i]:
                    print(i)
                    print(self.__graph[i])
                    print()

                    visited[i] = True

                    for j in range(self.vertex_quantity):
                        if self.__graph[i][j] == 1:
                            visit(visited_recursive)

        visit(visited)