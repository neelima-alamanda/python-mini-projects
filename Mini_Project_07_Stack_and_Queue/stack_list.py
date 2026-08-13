class Stack:
    """
    Represents a Stack using a Python list.
    Follows the Last-In-First-Out (LIFO) principle, where the last element added
    is the first element removed.
    """

    def __init__(self):
        """
        Initialize the stack as an empty list.
        self.stack: A list that stores the elements of the stack.
        """
        self.stack = []

    def push(self, item):
        """
        Add an element to the top of the stack.

        Args:
        - item: The value to be added to the stack.
        
        Operation:
        Append the given item to the end of the list,
        simulating the "push" operation in a stack.

        Time Complexity: O(1)
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Operation:
        Simulates the "pop" operation in a stack by removing the last item added.

        Returns:
        - The top element of the stack if it is not empty.
        - "Stack is empty" if the stack is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():  # Check if the stack is empty before popping
            return "Stack is empty"  # Edge case: Prevent accessing an empty stack
        return self.stack.pop()  # Remove and return the last element

    def peek(self):
        """
        Return the top element of the stack without removing it.
        
        Operation:
        Simulates the "peek" operation in a stack.

        Returns:
        - The top element of the stack if it is not empty.
        - "Stack is empty" if the stack is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():  # Check if the stack is empty before peeking
            return "Stack is empty"  # Edge case: Prevent returning from an empty stack
        return self.stack[-1]  # Return the last element without removing it

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        - True if the list (stack) has no elements.
        - False if the list contains elements.

        Time Complexity: O(1)
        """
        return len(self.stack) == 0  # A stack is empty if its length is 0


# Driver Code: Testing the Stack functionality
# This section simulates using the stack by adding, removing, and inspecting elements.

# Instantiate the stack
stack = Stack()

# Push elements onto the stack (add elements)
stack.push(10)  # Push 10 onto the stack
print("10 pushed into the stack.")  # Log the operation for clarity
stack.push(20)  # Push 20 onto the stack
print("20 pushed into the stack.")  # Log the operation for clarity
stack.push(30)  # Push 30 onto the stack
print("30 pushed into the stack.")  # Log the operation for clarity

# Peek at the top of the stack without removing the element
print("Top of the element:",stack.peek())  # Expected output: 30 (topmost element)

# Pop an element from the stack (remove from top)
print("popped element:",stack.pop())  # Expected output: 30 (last pushed element removed)

# Peek again to verify the new top element
print("Top of the element",stack.peek())  # Expected output: 20 (the new topmost element after popping 30)

# Check if the stack is empty
print("Is Stack Empty?", stack.is_empty())  # Expected output: False (stack is not empty)
print("Current stack:",stack.stack)