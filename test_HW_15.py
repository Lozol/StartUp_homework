# 1. Використовуючи код домашнього завдання 1 лекції 11, додайте до серверу чату систему логування рівня
# INFO WARNING ERROR
#


#  2. Взявши за основу код домашнього завдання лекції 14 , розробіть набір тестів з використанням бібліотеки
#  pytest для методів додавання нових елементів , пошуку мінімального і максимального значень та видалення
#  елементів бінарного дерева

import pytest

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


class TestTree():
    def setUp(self):
        self.tree = Tree(1)
        self.tree.left = Tree(2)
        self.tree.left.left = Tree(3)
        self.tree.left.right = Tree(4)
        self.tree.right = Tree(5)

    def test_init(self):
        assert type(self.tree.left) == "class '__main__.Tree'"

    def test_compare_min(self,tree):
        f1 = min_in_oder(self)
        assert f1 == 3

    def test_compare_max(self,tree):
        f1 = max_in_oder(self)
        assert f1 == 5





