class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    def display(self):
        self._display_recursive(self.root, 0)

    def _display_recursive(self, node, level):
        if not node:
            return
        self._display_recursive(node.right, level + 1)
        print('    ' * level + str(node.key))
        self._display_recursive(node.left, level + 1)

# Example usage:

bst = BST()
elements = [10, 5, 3, 7, 15, 12, 17]

for element in elements:
    bst.insert(element)

bst.display()
print(f"Height of the tree: {bst.height()}")

