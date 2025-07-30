#from tree_task import tree
from tree import Tree

print("1) Вставка:")
tree = Tree()

root = None

root = tree.insert(root, 3)
print(root.data)
tree.insert(root, 10)
tree.insert(root, 1)
tree.insert(root, 11)
tree.insert(root, 6)

tree.insert(root, 14)
tree.insert(root, 4)

print("5) Обход в глубину с рекурсией:")
tree.width_first_search_recursive(root)

tree.insert(root, 7)
tree.insert(root, 13)
tree.insert(root, 5)

print("Поиск родительского звена:")
#print(tree.search_parent_node(root, 13))

print("2) Поиск узла:")
print("root", root.data)
tree.search(root, 11)
tree.search(root, 13)
tree.search(root, 5)
tree.search(root, 3)
tree.search(root, 7)
tree.search(root, 10)
tree.search(root, 20)

print("5) Обход в ширину:")
tree.breadth_first_search(root)
print()

print("5) Обход в глубину:")
tree.width_first_search(root)

print("5) Обход в глубину с рекурсией:")
tree.width_first_search_recursive(root)

tree1 = Tree()

root1 = None

root1 = tree1.insert(root1, 3)

print("3) Удалить первое вхождение узла по значению:")
#tree.delete_by_value(root, 3)
#tree.breadth_first_search()

#tree.delete_by_value(root, 5)

tree.delete_by_value(root, 6)

print("5) Обход в ширину:")
tree.breadth_first_search(root)
print()

#tree.breadth_first_search()"""

print("Жопа")
tree.search(root, 11)
print("Жопа")
tree.delete_by_value(root, 11)
tree.search(root, 11)
#tree.breadth_first_search()
tree.breadth_first_search(root)

print("4) Получение числа элементов:")
print(tree.get_nodes_count(root))
