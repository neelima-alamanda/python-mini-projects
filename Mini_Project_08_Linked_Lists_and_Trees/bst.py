from collections import deque

class Node:
    # Node class represents each node in the Binary Search Tree.
    def __init__(self, data):
        self.data = data      # Value stored in the node.
        self.left = None      # Pointer to the left child node.
        self.right = None     # Pointer to the right child node.


class BinarySearchTree:
    # Class to implement a Binary Search Tree (BST).
    def __init__(self):
        self.root = None      # Root node of the BST.

    def is_empty(self):
        # Check if the tree is empty.
        return self.root is None

    def insert(self, data):
        # Inserts a new value in the tree, ensuring BST conditions are maintained.

        if self.search(data):   # Check and disallow duplicate values.
            print("Duplicate values are not allowed.")
            return

        self.root = self._insert(self.root, data)
        print("Node inserted successfully")

    def _insert(self, root, data):
        # Recursive helper to find position and insert the new node.
        if root is None:        # If the subtree is empty, create a new node.
            return Node(data)

        if data < root.data:    # Insert in the left subtree if data is smaller.
            root.left = self._insert(root.left, data)
        elif data > root.data:  # Insert in the right subtree if data is larger.
            root.right = self._insert(root.right, data)

        return root

    def search(self, element):
        # Public method to check if a value exists in the BST.
        return self._search(self.root, element)

    def _search(self, root, element):
        # Recursive helper function to search for a value in the tree.
        if root is None:        # If the node is null, the value is not found.
            return False

        if root.data == element:    # Value matches the current node's data.
            return True

        if element < root.data:     # Search in the left subtree.
            return self._search(root.left, element)

        return self._search(root.right, element)  # Search in the right subtree.

    def delete(self, data):
        # Deletes a value from the tree if it exists.
        if not self.search(data):          # Confirm the node exists before attempting deletion.
            print("Node not found")
            return

        self.root = self._delete(self.root, data)
        print("Node deleted successfully")

    def _delete(self, root, data):
        # Recursive helper function to find and delete a node.
        if root is None:                   # If tree is empty or null.
            return root

        if data < root.data:               # Traverse left subtree.
            root.left = self._delete(root.left, data)

        elif data > root.data:             # Traverse right subtree.
            root.right = self._delete(root.right, data)

        else:
            # If node found (data == root.data)

            # Case 1: Node has no children.
            if root.left is None and root.right is None:
                return None

            # Case 2: Node has one child.
            elif root.left is None:        # If left child is null, return the right child.
                return root.right
            elif root.right is None:       # If right child is null, return the left child.
                return root.left

            # Case 3: Node has two children.
            successor = self.find_min(root.right)  # Find the inorder successor (smallest element in right subtree).
            root.data = successor.data             # Replace current node's value with successor's value.
            root.right = self._delete(root.right, successor.data)  # Delete successor node.

        return root

    def find_min(self, root):
        # Finds the minimum value in a subtree.
        while root.left:  # Traverse to the leftmost node.
            root = root.left
        return root

    def inorder(self):
        # Public method for inorder traversal (Left -> Root -> Right).
        if self.is_empty():
            print("Tree is Empty")
            return

        print("Inorder Traversal:", end=" ")
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        # Recursive helper for inorder traversal.
        if root:
            self._inorder(root.left)      # Visit left subtree.
            print(root.data, end=" ")     # Print the current node.
            self._inorder(root.right)     # Visit right subtree.

    def preorder(self):
        # Public method for preorder traversal (Root -> Left -> Right).
        if self.is_empty():
            print("Tree is Empty")
            return

        print("Preorder Traversal:", end=" ")
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        # Recursive helper for preorder traversal.
        if root:
            print(root.data, end=" ")     # Print the current node.
            self._preorder(root.left)     # Visit the left subtree.
            self._preorder(root.right)    # Visit the right subtree.

    def postorder(self):
        # Public method for postorder traversal (Left -> Right -> Root).
        if self.is_empty():
            print("Tree is Empty")
            return

        print("Postorder Traversal:", end=" ")
        self._postorder(self.root)
        print()

    def _postorder(self, root):
        # Recursive helper for postorder traversal.
        if root:
            self._postorder(root.left)    # Visit the left subtree.
            self._postorder(root.right)   # Visit the right subtree.
            print(root.data, end=" ")     # Print the current node.

    def level_order(self):
        # Displays the tree using level-order traversal (Breadth-First Search).
        if self.root is None:
            print("Tree is Empty")
            return

        print("Level Order Traversal:", end=" ")

        queue = deque()                  # Initialize a queue for level-order traversal.
        queue.append(self.root)

        while queue:                     # Traverse while there are nodes in the queue.
            current = queue.popleft()    # Pop the front node from the queue.
            print(current.data, end=" ")

            if current.left:             # Add left child to the queue.
                queue.append(current.left)

            if current.right:            # Add right child to the queue.
                queue.append(current.right)

        print()


if __name__ == "__main__":
    bst = BinarySearchTree()

    print("=" * 55)
    print("      BINARY SEARCH TREE DEMONSTRATION")
    print("=" * 55)

    # Insert Operations
    print("\nInserting Nodes...")

    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # Search Operation
    print("\nSearching for Element 40...")

    if bst.search(40):
        print("Element Found")
    else:
        print("Element Not Found")

    # Traversals
    print("\nDisplaying Tree Traversals...\n")

    bst.inorder()
    bst.preorder()
    bst.postorder()
    bst.level_order()

    # Delete Operation
    print("\nDeleting Node 30...")
    bst.delete(30)

    print("\nTraversals After Deletion...\n")

    bst.inorder()
    bst.preorder()
    bst.postorder()
    bst.level_order()

    print("\nProgram Executed Successfully.")