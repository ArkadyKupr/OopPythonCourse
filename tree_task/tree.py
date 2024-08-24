from queue import Queue


class TreeNode:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None


@property
def data(self):
    return self.__data


@property
def left(self):
    return self.__left


@left.setter
def left(self, left):
    self.__left = left


@property
def right(self):
    return self.__right


@right.setter
def right(self, right):
    self.__right = right


# 1) Вставка:
def insert(self, data):
    if not isinstance(data, (int, float)):
        raise TypeError(f"Тип {data} должен быть int или float."
                        f"Сейчас: {type(data).__name__}")

    if data < self.__data:
        if self.__left is not None:
            return self.__left.insert(data)

        self.__left = TreeNode(data)
    else:
        if self.__right is not None:
            return self.__right.insert(data)

    self.__right = TreeNode(data)

    # 2) Поиск узла по значению:
    def search(self, data):
        if not isinstance(data, (int, float)):
            raise TypeError(f"Тип {data} должен быть int или float."
                            f"Сейчас: {type(data).__name__}")

        if data == self.__data:
            return self

        if data < self.__data:
            if self.__left is not None:
                return self.__left.search(data)

            return False

        if self.__right is not None:
            return self.__right.search(data)

            return False

            # 2) Поиск узла по адресу ребенка:
            def search_by_child(self, other, data):

                if not isinstance(self, TreeNode):
                    raise TypeError(f"{self} должен быть объектом TreeNode."
                    f"Сейчас: {type(self).__name__}")

                           if not isinstance(other, TreeNode):
                                   raise TypeError(f"{other} должен быть объектом TreeNode."
                                                   f"Сейчас: {type(other).__name__}")

                                 # 3.1) Удаление листа:
                               if other.__left is None and other.__right is None:
                                       if self.__left == other:
                                               self.__left = None
                                       return

                                   if self.__right == other:
                                           self.__right = None
                                       return

                                   if data < self.__data:
                                           return self.__left.search_by_child(other, data)

                                   return self.__right.search_by_child(other, data)

                                 # 3.2) Удаление узла с одним ребенком:
                               if not other.__left or not other.__right:
                                       if self.__left == other:
                                               self.__left = other.__left if other.__left else other.__right
                                       return

                                   if self.__right == other:
                                           self.__right = other.__left if other.__left else other.__right
                                       return

                                   if data < self.__data:
                                           if self.__left is not None:
                                                   return self.__left.search_by_child(other, data)

                                   if self.__right is not None:
                                           return self.__right.search_by_child(other, data)

                                 # 3.2) Удаление узла с двумя детьми:
                               if other.__left is not None and other.__right is not None:
                                       node = other.__right
                                   previous_node = node

                                   while node.__left is not None:
                                           previous_node = node
                                       node = node.__left

                                     # Удаление, когда у самого левого узла поддерева нет правого ребенка
                                   if node.__right is None:
                                           if self.__left == other:
                                                   node.__left = other.__left
                                           node.__right = other.__right

                                           self.__left = node

                                           previous_node.__left = None
                                           return

                                       if self.__right == other:
                                               node.__left = other.__left
                                           node.__right = other.__right

                                           self.__right = node

                                           previous_node.__left = None
                                           return

                                       if data < self.__data:
                                               if self.__left is not None:
                                                       return self.__left.search_by_child(other, data)

                                       if self.__right is not None:
                                               return self.__right.search_by_child(other, data)

                                     # Удаление, когда у самого левого узла поддерева есть правый ребенок

                                   if node.__right:
                                           if self.__left == other:
                                                   node.__left = other.__left
                                           right_child_of_most_left_node = node.__right
                                           node.__right = other.__right

                                           self.__left = node

                                           previous_node.__left = right_child_of_most_left_node
                                           return

                                       if self.__right == other:
                                               node.__left = other.__left
                                           right_child_of_most_left_node = node.__right
                                           node.__right = other.__right

                                           self.__right = node

                                           previous_node.__left = right_child_of_most_left_node
                                           return

                                       if data < self.__data:
                                               if self.__left is not None:
                                                       return self.__left.search_by_child(other, data)

                                       if self.__right is not None:
                                               return self.__right.search_by_child(other, data)

                             # 3) Удаление первого узла по значению
                           

                        def delete_first_by_value(self, data):

                                   if not isinstance(data, (int, float)):
                                           raise TypeError(f"Тип {data} должен быть int или float."
                                                           f"Сейчас: {type(data).__name__}")

                                       if self.__data == data and self.__left is None and self.__right is None:
                                               self.__data = None
                                           return

                                       child = self.search(data)

                                       self.search_by_child(child, data)

                                     # 5) Обход в ширину
                                     # Использование очереди
                                   

                                def breadth_first_search(self):

                                           nodes_queue = Queue()

                                       nodes_queue.put(self)

                                       while not nodes_queue.empty():
                                               node = nodes_queue.get()
                                           print(node.data)
                                           if node.left is not None:
                                                   nodes_queue.put(node.left)

                                           if node.right is not None:
                                                   nodes_queue.put(node.right)

                                     # 5) Обход в глубину без рекурсии
                                     # Использование стека. В Pythone нет реализации стека: использовать либо список, либо deque
                                   

                                def width_first_search(self):

                                    stack = []

                                # 1. Положить в стек корень дерева
                                stack.append(self)

                                while len(stack) > 0:
                                    first_item = stack.pop()
                                print(first_item.data)

                                if first_item.right is not None:
                                    stack.append(first_item.right)

                                if first_item.left is not None:
                                    stack.append(first_item.left)

                                # 5) Обход в глубину с рекурсией
                                def width_first_search_recursive(self):

                                    def visit(node):
                                        if not node:
                                            return

                                print(node.data)

                                visit(node.left)
                                visit(node.right)

                                visit(self)

                                # 4) Получение числа элементов:
                                def get_nodes_count(self):

                                # Использование breadth_first_search
                                nodes_queue = Queue()

                                nodes_queue.put(self)

                                nodes_count = 0
                                while not nodes_queue.empty():
                                    node = nodes_queue.get()
                                    nodes_count += 1

                                    if node.left is not None:
                                        nodes_queue.put(node.left)

                                if node.right is not None:
                                    nodes_queue.put(node.right)

                                return nodes_count


