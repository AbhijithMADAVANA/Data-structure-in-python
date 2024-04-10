class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print("The data is found")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Not found")

    def delete(self, data, curr):
        if self.key is None:
            print("Empty")
            return
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print("Not found")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Not found")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)
        return self

    def pre_order(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.in_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, end=" ")

    def min_value(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Min:", current.key)

    def max_value(self):
        max_val = self
        while max_val.rchild:
            max_val = max_val.rchild
        print("Max:", max_val.key)

    def is_identical(self, other):
        if not other:
            return False
        return self._is_identical(self, other)

    def _is_identical(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.key == node2.key:
            return (
                self._is_identical(node1.lchild, node2.lchild) and
                self._is_identical(node1.rchild, node2.rchild)
            )
        return False

    def height(self):
        return self._height(self)

    def _height(self, node):
        if not node:
            return 0
        left_height = self._height(node.lchild)
        right_height = self._height(node.rchild)
        return max(left_height, right_height) + 1


# Example usage:

# Create first BST
root1 = BST(10)
l1 = [3, 56, 34, 0, 12, 89]
for i in l1:
    root1.insert(i)

# Create second BST
root2 = BST(10)
l2 = [3, 56, 34, 0, 12, 89]
for i in l2:
    root2.insert(i)

# Check if trees are identical
if root1.is_identical(root2):
    print("Trees are identical")
else:
    print("Trees are not identical")

# Find height of the first tree
print("Height of the first tree:", root1.height())

# Perform other operations (search, delete, etc.) as needed
