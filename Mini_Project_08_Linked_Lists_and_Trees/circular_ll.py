class Node:
    # Node class represents each element in the circular linked list.
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node
        self.data = data
        self.next = None

class CircularLinkedList:
    # Class to implement a circular linked list with head, tail, and size.
    def __init__(self):
        # Initialize the circular linked list
        self.head = None  # Points to the first node
        self.tail = None  # Points to the last node
        self.size = 0     # Tracks the size of the list

    def is_empty(self):
        # Check if the list is empty
        return self.size == 0

    def insert_beginning(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(data)
        if self.is_empty():  # If the list is empty, initialize head and tail
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # Complete the circular reference
        else:  # Insert before the current head and update pointers
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head  # Maintain circular structure
        self.size += 1
        print("Node inserted successfully")

    def insert_end(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)
        if self.is_empty():  # If the list is empty, initialize head and tail
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:  # Append after the current tail and update pointers
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1
        print("Node inserted successfully")

    def insert_position(self, pos, data):
        # Insert a new node at the specified position
        if pos < 0 or pos > self.size:  # Validate position
            print("Invalid Position")
            return
        if pos == 0:  # Insert at the beginning
            self.insert_beginning(data)
            return
        if pos == self.size:  # Insert at the end
            self.insert_end(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(pos - 1):  # Traverse to the position
            current = current.next
        new_node.next = current.next  # Insert node at the position
        current.next = new_node
        self.size += 1
        print("Node inserted successfully")

    def delete_beginning(self):
        # Deletes the first node of the list
        if self.is_empty():  # Handle empty list
            print("Linked List is Empty")
            return
        if self.head == self.tail:  # If only one node, reset head and tail
            self.head = None
            self.tail = None
        else:  # Update head and maintain the circular link
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        print("Node deleted successfully")

    def delete_end(self):
        # Deletes the last node of the list
        if self.is_empty():  # Handle empty list
            print("Linked List is Empty")
            return
        if self.head == self.tail:  # If only one node, reset head and tail
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:  # Traverse to second last node
                current = current.next
            current.next = self.head  # Maintain circular link
            self.tail = current
        self.size -= 1
        print("Node deleted successfully")

    def delete_position(self, pos):
        # Deletes the node at the specified position
        if pos < 0 or pos >= self.size:  # Validate position
            print("Invalid Position")
            return
        if pos == 0:  # Delete from the beginning
            self.delete_beginning()
            return
        if pos == self.size - 1:  # Delete from the end
            self.delete_end()
            return
        current = self.head
        for i in range(pos - 1):  # Traverse to the position
            current = current.next
        current.next = current.next.next  # Bypass the node to delete it
        self.size -= 1
        print("Node deleted successfully")

    def search(self, element):
        # Searches for an element in the circular linked list
        if self.is_empty():  # Handle empty list
            return -1
        current = self.head
        position = 0
        while True:
            if current.data == element:  # If element found, return its position
                return position
            current = current.next
            position += 1
            if current == self.head:  # Stop once the list loops back to head
                break
        return -1  # Element not found

    def display(self):
        # Displays all elements in the circular linked list in order
        if self.is_empty():  # Handle empty list
            print("Linked List is Empty")
            return
        print(f"Circular Linked List (Size: {self.size})")
        current = self.head
        while True:
            # Display node data with indication for head and tail
            if current == self.head:
                print(f"[HEAD: {current.data}]", end=" -> ")
            elif current == self.tail:
                print(f"[TAIL: {current.data}]", end=" -> ")
            else:
                print(f"[{current.data}]", end=" -> ")
            current = current.next
            if current == self.head:  # Stop loop when back to head
                break
        print("(Back to HEAD)")

if __name__ == "__main__":
    cll = CircularLinkedList()

    print("=" * 55)
    print("      CIRCULAR LINKED LIST DEMONSTRATION")
    print("=" * 55)

    # Insert Operations
    print("\nInserting Nodes...")

    cll.insert_beginning(20)
    cll.insert_beginning(10)
    cll.insert_end(40)
    cll.insert_end(50)
    cll.insert_position(2, 30)

    print("\nCircular Linked List after Insert Operations:")
    cll.display()

    # Search Operation
    print("\nSearching for Element 30...")
    position = cll.search(30)

    if position != -1:
        print(f"Element Found at Position {position + 1}")
    else:
        print("Element Not Found")

    # Delete Beginning
    print("\nDeleting First Node...")
    cll.delete_beginning()

    print("\nCircular Linked List after Deleting First Node:")
    cll.display()

    # Delete End
    print("\nDeleting Last Node...")
    cll.delete_end()

    print("\nCircular Linked List after Deleting Last Node:")
    cll.display()

    # Delete Position
    print("\nDeleting Node at Position 2...")
    cll.delete_position(1)      # Position 2 (0-based index = 1)

    print("\nFinal Circular Linked List:")
    cll.display()

    print("\nProgram Executed Successfully.")