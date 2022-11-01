"""
implement red black tree
"""
from Node import Node


class RedBlackTree:
    def __init__(self):
        """
        initialize a red black tree
        """
        # initialize tree head
        self.tree = Node(float("inf"), None, color=False)
        # initialize root node
        self.tree.setLeft(self._initializeNewNode())
        self.tree.setRight(Node(None, None))
        self.tree.left.setBlack()

    @staticmethod
    def _initializeNewNode(value=None):
        """
        construct a new red node with two black leaves
        :return: the constructed new node
        """
        node = Node(value, None, color=True)
        node.setLeft(Node(None, None))
        node.setRight(Node(None, None))
        if value is not None:
            node.updateElementsNumber()
        return node

    def _balanceRotation(self, current_node):
        """
        blance the tree
        :return:
        """

        def _leftLeft(node):
            """
            case1: node is its father's left child, node and its father are both red and the node's father is its father's left child
            :param node: the current node
            :return: the root node of balanced subtree
            """
            # obtain the father of the node
            node_father = node.father
            # obtain the root of the subtree
            subtree_root = node_father.father
            # obtain the father of the subtree
            subtree_father = subtree_root.father
            # set node_father as the root node of the sub tree
            # check wheter the subtree is left or right childrenn of subtree_father
            if subtree_root.value <= subtree_father.value:
                # left
                subtree_father.setLeft(node_father)
            else:
                # right
                subtree_father.setRight(node_father)
            # set the right children of node.father as subtree_father's left children
            subtree_root.setLeft(node_father.right)
            # set subtree_father as the right children of node.father
            node_father.setRight(subtree_root)
            # change the color of node
            node.setBlack()
            # update elements number
            subtree_root.updateElementsNumber()
            node_father.updateElementsNumber()
            return node_father

        def _rightLeft(node):
            """
            case2: node is its father's right child, node and its father are both red, and the node's father is its father's left child
            :param node: the current node
            :return: the root node of balanced subtree
            """
            # obtain the father of the node
            node_father = node.father
            # obtain the root of the subtree
            subtree_root = node_father.father
            # obtain the father of the subtree
            subtree_father = subtree_root.father
            # set node as the root node of the sub tree
            # check wheter the subtree is left or right childrenn of subtree_father
            if subtree_root.value <= subtree_father.value:
                # left
                subtree_father.setLeft(node)
            else:
                # right
                subtree_father.setRight(node)
            # set node's left children as the right children of node_father
            node_father.setRight(node.left)
            # set node's right children as the left children of subtree_root
            subtree_root.setLeft(node.right)
            # set subtree_root as node's right children
            node.setRight(subtree_root)
            # set node_father as node's left children
            node.setLeft(node_father)
            # change the color of node_father
            node_father.setBlack()
            # update elements number
            subtree_root.updateElementsNumber()
            node_father.updateElementsNumber()
            node.updateElementsNumber()
            return node

        def _rightRight(node):
            """
            case3: node is its father's right child, node and its father are both red and the node's father is its father's right child
            :param node: the current node
            :return: the root node of balanced subtree
            """
            # obtain the father of the node
            node_father = node.father
            # obtain the root of the subtree
            subtree_root = node_father.father
            # obtain the father of the subtree
            subtree_father = subtree_root.father
            # set node_father as the root node of the sub tree
            # check whether the subtree is left or right children of subtree_father
            if subtree_root.value <= subtree_father.value:
                # left
                subtree_father.setLeft(node_father)
            else:
                # right
                subtree_father.setRight(node_father)
            # set the left children of node_father as subtree_father's right children
            subtree_root.setRight(node_father.left)
            # set subtree_father as the left children of node.father
            node_father.setLeft(subtree_root)
            # change the color of node
            node.setBlack()
            # update elements number
            subtree_root.updateElementsNumber()
            node_father.updateElementsNumber()
            return node_father

        def _leftRight(node):
            """
            case4: node is its father's left child, node and its father are both red, and the node's father is its father's right child
            :param node: the current node
            :return: the root node of balanced subtree
            """
            # obtain the father of the node
            node_father = node.father
            # obtain the root of the subtree
            subtree_root = node_father.father
            # obtain the father of the subtree
            subtree_father = subtree_root.father
            # set node as the root node of the sub tree
            # check wheter the subtree is left or right childrenn of subtree_father
            if subtree_root.value <= subtree_father.value:
                # left
                subtree_father.setLeft(node)
            else:
                # right
                subtree_father.setRight(node)
            # set node's right children as the left children of node_father
            node_father.setLeft(node.right)
            # set node's left children as the right children of subtree_root
            subtree_root.setRight(node.left)
            # set subtree_root as node's left children
            node.setLeft(subtree_root)
            # set node_father as node's right children
            node.setRight(node_father)
            # change the color of node_father
            node_father.setBlack()
            # update elements number
            subtree_root.updateElementsNumber()
            node_father.updateElementsNumber()
            node.updateElementsNumber()
            return node

        # judge if the current node is root node
        if current_node.father.father is None:
            # paint current node black
            if current_node.judgeRed():
                current_node.setBlack()
            return
        # balance the tree
        # when two consecutive red nodes occur
        if current_node.judgeRed() and current_node.father.judgeRed():
            if current_node.father.value <= current_node.father.father.value:
                # the node's father is its father's left child
                if current_node.value <= current_node.father.value:
                    # case1: the node is its father's left child
                    next_node =  _leftLeft(current_node)
                else:
                    # case2: the node is its father's right child
                    next_node = _rightLeft(current_node)
            else:
                # the node's father is its father's right child
                if current_node.value > current_node.father.value:
                    # case3: the node is its father's right child
                    next_node = _rightRight(current_node)
                else:
                    # case4: the node is its father's left child
                    next_node = _leftRight(current_node)
        else:
            next_node = current_node.father
        self._balanceRotation(next_node)

    def delete(self, data):
        """
        delete the element with the value of data
        :param data: the value to be deleted
        :return:
        """

        def delete_leaf(leaf):
            """
            delete the node (maybe a leaf) in the red-black tree
            :param leaf: the leaf to be deleted
            :return:
            """
            # when leaf is red, just delete it
            if leaf.judgeRed():
                if leaf.value <= leaf.father.value:
                    leaf.father.setLeft(Node(None, None))
                else:
                    leaf.father.setRight(Node(None, None))
                # update elements number
                update_scale(leaf.father)
            else:
                # when leaf is black
                # if leaf have no child
                if leaf.right.judgeLeaf():
                    if leaf.value <= leaf.father.value:
                        leaf.father.setLeft(Node(None, None))
                        update_scale(leaf.father)
                        balanceLeft(leaf.father.left)
                    else:
                        leaf.father.setRight(Node(None, None))
                        update_scale(leaf.father)
                        balanceRight(leaf.father.right)
                else:
                    # just paint the right child black and delete leaf
                    leaf.right.setBlack()
                    # delete leaf
                    if leaf.value <= leaf.father.value:
                        leaf.father.setLeft(leaf.right)
                    else:
                        leaf.father.setRight(leaf.right)
                    update_scale(leaf.father)
            # detach leaf
            leaf_value = leaf.value
            del leaf
            return leaf_value

        def update_scale(node):
            """
            update the number of elements in the subtree
            :param node: the root of a subtree
            :return:
            """
            node.updateElementsNumber()
            if node.father is None:
                return
            if node.father.father is None:
                return
            else:
                update_scale(node.father)

        def balanceLeft(node):
            """
            balance if left children's black height is one less than that of right children
            :param node:
            :return:
            """
            # judge if the node is root node
            if node.father.father is None:
                # paint node black
                if node.judgeRed():
                    node.setBlack()
                return
            # if node's right brother is black
            if not node.father.right.judgeRed():
                # if node's brother's children is black
                if (not node.father.right.left.judgeRed()) and (not node.father.right.right.judgeRed()):
                    # if node's father is black
                    if not node.father.judgeRed():
                        # paint node's brother red
                        node.father.right.setRed()
                        # node's father is the root of the subtree to be balanced
                        if node.father.value <= node.father.father.value:
                            balanceLeft(node.father)
                        else:
                            balanceRight(node.father)
                    else:
                        # swap the color between node's brother an d node's father
                        swapColor(node.father, node.father.right)
                else:
                    if node.father.right.right.judgeRed():
                        leftRotate(node.father)
                    else:
                        rightRotate(node.father.right)
                        balanceLeft(node)
            else:
                leftRotate(node.father)
                balanceLeft(node)

        def balanceRight(node):
            """
            balance if left children's black height is one more than that of right children
            :param node:
            :return:
            """
            # judge if the node is root node
            if node.father.father is None:
                # paint node black
                if node.judgeRed():
                    node.setBlack()
                return
            # if node's left brother is black
            if not node.father.left.judgeRed():
                # if node's brother's children is black
                if (not node.father.left.left.judgeRed()) and (not node.father.left.right.judgeRed()):
                    # if node's father is black
                    if not node.father.judgeRed():
                        # paint node's brother red
                        node.father.left.setRed()
                        # node's father is the root of the subtree to be balanced
                        if node.father.value <= node.father.father.value:
                            balanceLeft(node.father)
                        else:
                            balanceRight(node.father)
                    else:
                        # swap the color between node's brother an d node's father
                        swapColor(node.father, node.father.left)
                else:
                    if node.father.left.left.judgeRed():
                        rightRotate(node.father)
                    else:
                        leftRotate(node.father.left)
                        balanceRight(node)
            else:
                rightRotate(node.father)
                balanceRight(node)

        def leftRotate(node):
            """
            letf rotate the subtree
            :param node: the root of the sub tree
            :return:
            """
            # obtain subtree father
            subtree_father = node.father
            # obtain new root
            new_root = node.right
            # obtain new root's left child
            new_root_left = new_root.left
            # right rotate
            if node.value <= subtree_father.value:
                subtree_father.setLeft(new_root)
            else:
                subtree_father.setRight(new_root)
            node.setRight(new_root_left)
            new_root.setLeft(node)
            new_root.right.setBlack()
            swapColor(node, new_root)
            # update elements number
            node.updateElementsNumber()
            new_root.updateElementsNumber()

        def rightRotate(node):
            """
            right rotate the subtree
            :param node: the root of the sub tree
            :return:
            """
            # obtain subtree father
            subtree_father = node.father
            # obtain new root
            new_root = node.left
            # obtain new root's right child
            new_root_right = new_root.right
            # right rotate
            if node.value <= subtree_father.value:
                subtree_father.setLeft(new_root)
            else:
                subtree_father.setRight(new_root)
            node.setLeft(new_root_right)
            new_root.setRight(node)
            new_root.left.setBlack()
            swapColor(node, new_root)
            # update elements number
            node.updateElementsNumber()
            new_root.updateElementsNumber()

        def swapColor(node1, node2):
            """
            swap the color of two nodes
            :param node1:
            :param node2:
            :return:
            """
            # obtain the color if two node
            node1_color = node1.color
            node2_color = node2.color
            # swap color
            node1.setColor(node2_color)
            node2.setColor(node1_color)

        def _min(subtree):
            """
            return the min value of the subtree
            :return:
            """
            pointer = subtree
            while True:
                if pointer.left.value is None:
                    break
                else:
                    pointer = pointer.left
            return pointer

        # search if data to be deleted exists in the tree
        deletedData = self.search(data)
        # if the value exists
        if deletedData is not None:
            if deletedData.right.value is not None:
                # obtain the successive node
                successive_value = delete_leaf(_min(deletedData.right))
            else:
                # the deleted node is a leaf
                if deletedData.left.value is None:
                    delete_leaf(deletedData)
                    return
                # the deleted node has a red left child
                else:
                    successive_value = delete_leaf(deletedData.left)
            deletedData.value = successive_value

    def insert(self, data):
        """
        insert an element
        :param data: a new element
        :return:
        """

        def _judgeLeftOrRight(query_data, node):
            """
            judege a data to the left or right child
            :param query_data: the data
            :param node: the current node
            :return:
            """
            # update the number of elements in the subtree of current node
            node.addElementsNumber()

            if query_data <= node.value:
                # allocate data to left child of node
                if node.left.value is None:
                    # assign the left child with the value of query_data
                    del node.left
                    node.setLeft(self._initializeNewNode(query_data))
                    return node.left
                else:
                    return _judgeLeftOrRight(query_data, node.left)
            else:
                # allocate data to right child of node
                if node.right.value is None:
                    # assign the right child with the value of query_data
                    del node.right
                    node.setRight(self._initializeNewNode(query_data))
                    return node.right
                else:
                    return _judgeLeftOrRight(query_data, node.right)

        # assign the value to the root node if the tree is empty
        if self.tree.left.value is None:
            self.tree.setLeft(self._initializeNewNode())
            self.tree.left.setBlack()
            self.tree.left.value = data
            self.tree.left.updateElementsNumber()
            return
        # if data is not exists in the tree
        if self.search(data) is None:
            # obtain the handle of the new inserted node
            new_node = _judgeLeftOrRight(data, self.tree.left)
            self._balanceRotation(new_node)

    def traverse(self):
        """
        traverse the tree
        :return: results of all the values in the tree
        """

        def inOrderTraverse(node, results):
            """
            in-order traverse the tree
            :param results: a lists store values already traversed
            :param node: the root node of the subtree
            :return:
            """
            if node.value is None:
                return
            inOrderTraverse(node.left, results)
            results.append(node.value)
            inOrderTraverse(node.right, results)

        # initialize a result list
        results = []
        # traverse
        inOrderTraverse(self.tree.left, results)
        return results

    def median(self):
        """
        find the median value of the tree
        :return:
        """

        def indexing(sub_tree, index):
            """
            recursively find the value of the input tree indexed by a particular number
            :param sub_tree:
            :return:
            """
            if index == sub_tree.left.elements_number + 1:
                return sub_tree.value
            if index <= sub_tree.left.elements_number:
                return indexing(sub_tree.left, index)
            else:
                return indexing(sub_tree.right, index - sub_tree.left.elements_number - 1)

        # obtain the total number of elements in the red-black tree
        elements_number = self.tree.left.elements_number
        # even then return average value of the two middle values
        # odd then return the median value
        if elements_number % 2 == 0:
            # even
            index_left = elements_number / 2
            index_right = index_left + 1
            median_value = (indexing(self.tree.left, index_left) + indexing(self.tree.left, index_right)) / 2
            return median_value
        else:
            # odd
            index = int(elements_number / 2) + 1
            return indexing(self.tree.left, index)

    def min(self):
        """
        return the min value of the tree
        :return:
        """
        pointer = self.tree.left
        while True:
            if pointer.left.value is None:
                break
            else:
                pointer = pointer.left
        return pointer.value

    def max(self):
        """
        return the max value of the tree
        :return:
        """
        pointer = self.tree.left
        while True:
            if pointer.right.value is None:
                break
            else:
                pointer = pointer.right
        return pointer.value

    def search(self, query):
        """
        seach if a value exists in the tree
        :param query: a query value
        :return: the node with the value of query if the qyery exists in the tree, else None
        """
        pointer = self.tree.left
        while True:
            if pointer.value == query:
                return pointer
            elif query < pointer.value:
                if pointer.left.value is None:
                    return None
                else:
                    pointer = pointer.left
            else:
                if pointer.right.value is None:
                    return None
                else:
                    pointer = pointer.right

    def verify(self):
        """
        test if current tree is a red black tree
        :return:
        """

        def blackPathLength(node):
            """
            calculate the number of black nodes in the node's left children and right children
            :param node:
            :return: False if the tree is not a red black tree or the black height of the tree
            """
            if node.value is None:
                # if the node is a leaf
                return 1
            # judge if two consecutive red nodes exist
            if (node.left.judgeRed() and node.judgeRed()) or (node.right.judgeRed() and node.judgeRed()):
                return False
            # calculate the number of black node in the left path
            left_path_length = blackPathLength(node.left)
            # calculate the number of black node in the right path
            right_path_length = blackPathLength(node.right)
            # compare the number of black nodes in left path and right path\
            if isinstance(left_path_length, int) and isinstance(right_path_length, int):
                if left_path_length == right_path_length:
                    if not node.judgeRed():
                        return left_path_length + 1
                    else:
                        return left_path_length
                else:
                    return False
            else:
                return False

        def judge_upward():
            """
            judge if the elements is upward after in-order traverse
            :param node:
            :return:
            """
            sequences = self.traverse()
            for i in range(len(sequences)):
                if i + 1 == len(sequences):
                    break
                if sequences[i] > sequences[i+1]:
                    return False
            return True
        return (not self.tree.left.judgeRed()) and judge_upward(), blackPathLength(self.tree.left)


def intersection(tree1, tree2):
    """
    calculate the values both in red black tree1 and red black tree2
    :param tree1: the first red black tree
    :param tree2: the second red black tree
    :return:
    """
    # obtain all values in each tree with an upward order
    tree1_elements = tree1.traverse()
    tree2_elements = tree2.traverse()
    # obtain the muber of elements in the two trees
    tree1_length = tree1.tree.left.elements_number
    tree2_length = tree2.tree.left.elements_number
    # initialize intersection
    intersection_set = []
    i = 0  # tree1 index
    j = 0  # tree2 index
    while True:
        if i == tree1_length or j == tree2_length:
            break
        if tree1_elements[i] == tree2_elements[j]:
            intersection_set.append(tree1_elements[i])
            i += 1
            j += 1
        elif tree1_elements[i] < tree2_elements[j]:
            i += 1
        else:
            j += 1
    return intersection_set
