class Node:
    def __init__(self, data):
        # Initialize a Node with data and a pointer to the next node
        self.data = data
        self.next = None 

class Stack:
    def __init__(self):
        # Stack is initialized with an empty top pointer
        self.top = None 

    def is_empty(self):
        # Checks if the stack is empty by verifying if the top is None
        return self.top is None

    def push(self, data):
        # Create a new node and make it the new top of the stack
        new_node = Node(data)
        new_node.next = self.top  # Link the new node to the current top node
        self.top = new_node       # Update the top to be the new node

    def pop(self):
        # Removes and returns the top element of the stack
        if self.is_empty():        # Check if the stack is empty
            return "Stack is empty"
        popped_value = self.top.data  # Store the data of the top node
        self.top = self.top.next      # Move the top pointer to the next node
        return popped_value           # Return the popped value

    def peek(self):
        # Returns the top element of the stack without removing it
        if self.is_empty():        # Check if the stack is empty
            return "Stack is empty"
        return self.top.data       # Return the data of the top node

# Driver Code: Test the stack implementation

# Initialize a new stack
stack = Stack()

# Push elements into the stack
stack.push(10)  # Add 10 to the stack
stack.push(20)  # Add 20 to the stack
stack.push(30)  # Add 30 to the stack

# Display the top element
print("Top Element:", stack.peek())  # Expected: 30 (last pushed element)

# Remove the top element
print("Popped Element:", stack.pop())  # Expected: 30

# Display the top element after popping
print("Top Element after Pop:", stack.peek())  # Expected: 20

# Check whether the stack is empty
print("Is Stack Empty?", stack.is_empty())  # Expected: False (stack still has elements)