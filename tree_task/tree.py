from queue import Queue
from tree_node import TreeNode


class Tree:
    def __init__(self):
        self.__count = 0

    @property
    def count(self):
        return self.__count

    def create_node(self, data):
        self.__count += self.__count
        return TreeNode(data)

    # 1) Вставка:
    def insert(self, node, data):
        if not isinstance(data, (int, float)):
            raise TypeError(f"Тип {data} должен быть int или float."
                            f"Сейчас: {type(data).__name__}")

        if node is None:
            return self.create_node(data)

        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        return node

        # 2) Поиск узла по значению:
    def search(self, node, data):
        if not isinstance(data, (int, float)):
            raise TypeError(f"Тип {data} должен быть int или float."
                            f"Сейчас: {type(data).__name__}")

        if node is None:
            return None

        if node.data == data:
            return node.left

        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    # 2) Поиск узла по значению:
    def search_1(self, node, data):
        if not isinstance(data, (int, float)):
            raise TypeError(f"Тип {data} должен быть int или float."
                            f"Сейчас: {type(data).__name__}")

        if node.data == data:
            return node

        if node.left is not None and node.left.data == data:
            return node

        if node.right is not None and node.right.data == data:
            return node

        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    # 2) Поиск родительского узла по адресу ребенка:
    def search_parent_node(self, node, child):
        """if not isinstance(data, (int, float)):
            raise TypeError(f"Тип {data} должен быть int или float."
                            f"Сейчас: {type(data).__name__}")"""

        """if node is None:
            return None"""

        """if node.left is child or node.right is child:
            return node"""

        if node.left is not None and node.left.data == child.data:
            return node

        """if node.right is not None and node.right.data == child.data:
            return node"""

        if child.data < node.data:
            return self.search_parent_node(node.left, child)
        else:
            return self.search_parent_node(node.right, child)

    # 3) Удаление первого вхождения узла по значению
    def delete_by_value(self, node, data):
        if not isinstance(data, (int, float)):
            raise TypeError(f"Тип {data} должен быть int или float."
                            f"Сейчас: {type(data).__name__}")

        # случай удаления корня в дерева без детей
        if node.data == data and node.left is None and node.right is None:
            node.data = None
            print("Да, я удалил")
            return

        """if node.data == data:
            node.left = None
            node.right = None
            return"""

        # находим узел child, в котором содержится data
        child = self.search(node, data)
        print("Это то, что нашли", child.data)

        if child is not None:
            parent = self.search_parent_node(node, child)
        else:
            return


        # 3.1) Удаление листа:
        if child.left is None and child.right is None:
            print("Это отсюда")
            print("Это: ", parent.data)

            if parent.left is not None and parent.left == child:
                print("Отсюда left")
                parent.left = None
                return

            if parent.right is not None and parent.right == child:
                print("Отсюда right")
                parent.right = None
                return

        # 3.2) Удаление узла с одним ребенком:
        if child.left is None or child.right is None:
            print("Удаление узла с одним ребенком:")

            if parent.left == child:
                parent.left = child.left if child.left is not None else child.right
                return

            if parent.right == child:
                parent.right = child.right if child.right is not None else child.left
                return

        # 3.2) Удаление узла с двумя детьми:
        if child.left is not None and child.right is not None:
            print("Удаление узла с двумя детьми:")

            current_node = child.right
            previous_node = None

            while current_node.left is not None:
                previous_node = current_node
                current_node = current_node.left

            # Удаление, когда у самого левого узла поддерева нет правого ребенка
            # У родителя удаляемого узла подменяем ссылку с удаляемого узла на этот самый левый элемент
            if current_node.right is None:

                if parent.left == child:
                    parent.left = current_node

                    current_node.left = child.left
                    current_node.right = child.right

                    previous_node.left = None
                    return

                if parent.right == child:
                    parent.right = current_node

                    current_node.left = child.left
                    current_node.right = child.right

                    previous_node.left = None
                    return
            else:

                # Удаление, когда у самого левого узла поддерева есть правый ребенок
                # Если у самого левого узла был правый сын, то ставим его на место этого левого узла
                if parent.left == child:
                    parent.left = current_node

                    previous_node.left = current_node.right

                    current_node.left = child.left
                    current_node.right = child.right
                    return

                if parent.right == child:
                    parent.right = current_node

                    previous_node.left = current_node.right

                    current_node.left = child.left
                    current_node.right = child.right
                    return

    # 5) Обход в ширину
    # Использование очереди
    def breadth_first_search(self, node):
        nodes_queue = Queue()

        nodes_queue.put(node)

        while not nodes_queue.empty():
            node = nodes_queue.get()
            print(node.data)
            if node.left is not None:
                nodes_queue.put(node.left)

            if node.right is not None:
                nodes_queue.put(node.right)

    # 5) Обход в глубину без рекурсии
    # Использование стека. В Pythone нет реализации стека: использовать либо список, либо deque
    def width_first_search(self, node):
        stack = []

        # 1. Положить в стек корень дерева
        stack.append(node)

        while len(stack) > 0:
            first_item = stack.pop()
            print(first_item.data)

            if first_item.right is not None:
                stack.append(first_item.right)

            if first_item.left is not None:
                stack.append(first_item.left)

    # 5) Обход в глубину с рекурсией
    def width_first_search_recursive(self, node):
        def visit(node):
            if not node:
                return
            print(node.data)

            visit(node.left)
            visit(node.right)

        visit(node)

    # 4) Получение числа элементов:
    def get_nodes_count(self, node):
        # Использование breadth_first_search
        nodes_queue = Queue()

        nodes_queue.put(node)

        nodes_count = 0

        while not nodes_queue.empty():
            node = nodes_queue.get()
            nodes_count += 1

            if node.left is not None:
                nodes_queue.put(node.left)

            if node.right is not None:
                nodes_queue.put(node.right)

        return nodes_count
