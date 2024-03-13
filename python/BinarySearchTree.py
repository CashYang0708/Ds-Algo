class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    # insert new node to BST
    def insert(self, val: int) -> None:
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            self._insert(val, self.root)

    def _insert(self, val: int, curr_node: Node):
        node = Node(val)
        if val < curr_node.val:
            if not curr_node.left:
                curr_node.left = node
            else:
                self._insert(val, curr_node.left)
        elif val > curr_node.val:
            if not curr_node.right:
                curr_node.right = node
            else:
                self._insert(val, curr_node.right)
        else:
            print("value exists")

    # whether the value exist in this BST
    def _search(self, val: int, root: Node) -> bool:
        if not root:
            return False
        if root.val == val:
            return True
        elif root.val > val:
            self._search(val, root.left)
        else:
            self._search(val, root.right)
        return False

    def search(self, val: int):
        return self._search(val, self.root)

    # print whole elements in BST from small to big with inorder traversal
    def _print(self, root: Node) -> None:
        if not root:
            return
        else:
            self._print(root.left)
            print(root.val)
            self._print(root.right)

    def print_BST(self):
        self._print(self.root)

    # delete node with given value
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)

        return root


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(-10)
    tree.insert(33)
    tree.insert(0)
    tree.print_BST()
    print(tree.search(14))
    tree.delete(0)
    tree.print_BST()
