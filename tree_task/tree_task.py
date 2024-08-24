from tree_task.tree import TreeNode

print("1) Вставка:")
root = TreeNode(8)

print(root.data)

root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(14)
root.insert(4)
root.insert(7)
root.insert(13)
root.insert(5)
print(root.right.data)

print("2) Поиск узла:")
print(root.search(11))
print(root.search(13))

print("5) Обход в ширину:")
root.breadth_first_search()
print()

print("5) Обход в глубину:")
root.width_first_search()

print("5) Обход в глубину с рекурсией:")
root.width_first_search_recursive()

print("3) Удалить первое вхождение узла по значению:")
root.delete_first_by_value(3)
root.breadth_first_search()

root.delete_first_by_value(5)
root.breadth_first_search()

root.delete_first_by_value(10)
root.breadth_first_search()

print("4) Получение числа элементов:")
print(root.get_nodes_count())
