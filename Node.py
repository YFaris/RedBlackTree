"""
define the functions of nodes in red black tree
"""


class Node:
    def __init__(self, data, father, color=False):
        """
        a node of red-black tree
        """
        self.father = father  # father node of the current node
        self.color = color  # True is red, False is black
        self.value = data  # the value of the node
        self.left = None  # left child
        self.right = None  # right child
        self.elements_number = 0  # the sum number of elements in the left children, right children, and the node itself

    def addElementsNumber(self):
        """
        the number of elements add 1
        :return:
        """
        self.elements_number += 1

    def updateElementsNumber(self):
        """
        update the number of elements of the node's subtree has
        :return:
        """
        self.elements_number = self.left.elements_number + self.right.elements_number + 1

    def setLeft(self, left):
        """
        set the left child of the current node
        :param left: left child
        :return:
        """
        self.left = left
        left.father = self

    def setRight(self, right):
        """
        set the right child of the current node
        :param right: left child
        :return:
        """
        self.right = right
        right.father = self

    def setFather(self, father):
        """
        set father of current node
        :param father:
        :return:
        """
        self.father = father

    def setRed(self):
        """
        set red of self.color
        """
        self.color = True

    def setBlack(self):
        """
        set black of self.color
        """
        self.color = False

    def setColor(self, color):
        """
        set the color of the node as color
        :param color:
        :return:
        """
        self.color = color

    def judgeRed(self):
        """
        return True if the node is red, otherwise False
        :return:
        """
        return self.color

    def judgeLeaf(self):
        """
        return True if the value of the node is None
        :return:
        """
        return self.value is None
