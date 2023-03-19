#1. Додайте до класу Tree метод, який реалізує додавання до бінарного дерева пошуку нових елементів
# зі списку. Метод має містити функціонал, який перевіряє дані зі списку на відповідьність до правил
# формування бінарного дерева пошуку. ("Правильный" (с точки зрения ООП) способ добавить свои методы -
# создать свой класс, наследующийся от исходного стандартного класса.)
# class Tree:
#     def __init__(self, id_node):
#         self.id_node = id_node
#         self.left = None
#         self.right = None
#
#     def __str__(self):
#         return str(self.id_node)
#
#     #Insert metod to create nodes
#     def insert(self,id_node):
#         if self.id_node:
#             if id_node < self.id_node:
#                 if self.left is None:
#                     self.left = Tree(id_node)
#                 else:
#                     self.left.insert(id_node)
#             elif id_node>self.id_node:
#                 if self.right is None:
#                     self.right = Tree(id_node)
#                 else:
#                     self.right.insert(id_node)
#         else:
#             self.id_node = id_node


# 2. Додайте до класу Tree методи пошуку мінімального і максимального значення елементів в бінарному
# дереві пошуку
class Tree:
    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    #Insert metod to create nodes
    def insert(self,id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node>self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    def min_in_oder(self):
        if self.left:
            self.left.min_in_oder()
        else:
            print(self.id_node)

    def max_in_oder(self):
        if self.right:
            self.right.max_in_oder()
        else:
            print(self.id_node)


# 3. Розширте функціонал класу Tree , додавши в нього метод видалення елементів і бінарному дереві пошуку.

