from collections import deque

class Node:
    # Represents each node in the Binary Tree.
    def __init__(self, data):
        self.data = data          # Stores the value of the node.
        self.left = None          # Points to the left child.
        self.right = None         # Points to the right child.


class BinaryTree:
    # Implements a Binary Tree with insertion, balance check, and level-order display.
    def __init__(self):
        self.root = None          # Pointer to the root node of the tree.

    def is_empty(self):
        # Checks if the tree is empty.
        return self.root is None

    def insert(self, data):
        # Inserts a new node into the binary tree using level-order traversal.

        new_node = Node(data)     # Create a new node.
        if self.is_empty():       # If the tree is empty, set the new node as the root.
            self.root = new_node
            print("Node inserted successfully")
            return

        queue = deque()           # Use a queue for level-order traversal to find an empty spot.
        queue.append(self.root)

        while queue:
            current_node = queue.popleft()
            if current_node.left is None:         # Check if the left child is empty.
                current_node.left = new_node
                print("Node inserted successfully")
                return
            else:
                queue.append(current_node.left)   # Add the left child to the queue.

            if current_node.right is None:        # Check if the right child is empty.
                current_node.right = new_node
                print("Node inserted successfully")
                return
            else:
                queue.append(current_node.right)  # Add the right child to the queue.

    def check_balance(self, root):
        # Helper function to check balance and calculate the height.

        if root is None:          # An empty subtree is balanced with height 0.
            return 0

        left_height = self.check_balance(root.left)  # Check balance and height recursively for the left subtree.
        if left_height == -1:     # If left subtree is unbalanced, propagate -1.
            return -1

        right_height = self.check_balance(root.right)  # Check balance and height recursively for the right subtree.
        if right_height == -1:    # If right subtree is unbalanced, propagate -1.
            return -1

        if abs(left_height - right_height) > 1:   # If this node is unbalanced, return -1.
            return -1

        return 1 + max(left_height, right_height)  # Return the height of the current node.

    def is_balanced(self):
        # Public method to check if the binary tree is balanced.

        if self.is_empty():        # An empty tree is always balanced.
            return True

        return self.check_balance(self.root) != -1  # Balanced if `check_balance` doesn't return -1.

    def level_order_display(self):
        # Displays the tree in level-order (breadth-first) traversal.

        if self.is_empty():       # Check if the tree is empty.
            print("Tree is Empty")
            return
        
        print("Level Order Traversal:", end=" ")
        
        queue = deque()           # Use a queue for level-order traversal.
        queue.append(self.root)
        
        while queue:
            current_node = queue.popleft()        # Dequeue the front node.
            print(current_node.data, end=" ")     # Print the data of the current node.

            if current_node.left:                 # Enqueue the left child if it exists.
                queue.append(current_node.left)
            if current_node.right:                # Enqueue the right child if it exists.
                queue.append(current_node.right)

        print()


if __name__ == "__main__":
    tree = BinaryTree()

    print("=" * 60)
    print("        BALANCED BINARY TREE DEMONSTRATION")
    print("=" * 60)

    # Insert Nodes
    print("\nInserting Nodes...")

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(60)
    tree.insert(70)

    # Display Tree
    print("\nLevel Order Traversal of Binary Tree:")
    tree.level_order_display()

    # Check Balance
    print("\nChecking Whether the Binary Tree is Balanced...")

    if tree.is_balanced():
        print("The Binary Tree is Balanced.")
    else:
        print("The Binary Tree is NOT Balanced.")

    print("\nProgram Executed Successfully.")