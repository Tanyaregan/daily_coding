# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.


class BinaryTree(object):
    """A binary search tree"""

    def __init__(self, root):
        self.root = root


class BinaryTreeNode(object):
    """An node in a binary search tree"""

    def __init__(self, data, left=None, right=None):
        """Initializes node in a tree"""
        self.data = data
        self.left = left
        self.right = right

    def serialize(self, root):
        """given the root node, serializes binary tree into a string"""

        to_serialize = root
        serialized = []

        while to_serialize:
            current = to_serialize.pop()
            to_serialize.append(current.left)
            to_serialize.append(current.right)
            serialized.append(current)

        return serialized

    def deserialize(self, string):
        """given a string of BinaryTreeNodes, returns string to binary tree"""

        for item in string:
            if not item.left:
                root = string.pop(item)

        reserialized = BinaryTree(root, right=root.right)

        for item in string:
            reserialized.add(item)

        return reserialized
