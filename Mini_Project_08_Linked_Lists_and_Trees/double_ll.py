class Node:
    # Represents each node in the doubly linked list.
    def __init__(self, data):
        self.data = data      # Stores the value of the node.
        self.prev = None      # Points to the previous node.
        self.next = None      # Points to the next node.


class DoublyLinkedList:
    # Implements a doubly linked list with a head, tail, and size.
    def __init__(self):
        self.head = None      # Head points to the first node.
        self.tail = None      # Tail points to the last node.
        self.size = 0         # Tracks the number of nodes.

    def is_empty(self):
        # Checks if the list is empty.
        return self.size == 0

    def insert_beginning(self, data):
        # Inserts a node at the beginning of the list.
        new_node = Node(data)
        if self.is_empty():  # If list is empty, set head and tail.
            self.head = new_node
            self.tail = new_node
        else:  # Update head and link previous head.
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        print("Node inserted successfully")

    def insert_end(self, data):
        # Inserts a node at the end of the list.
        new_node = Node(data)
        if self.is_empty():  # If list is empty, set head and tail.
            self.head = new_node
            self.tail = new_node
        else:  # Update tail and link previous tail.
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        print("Node inserted successfully")

    def insert_position(self, pos, data):
        # Inserts a node at a specific position in the list.
        if pos < 0 or pos > self.size:  # Validate position.
            print("Invalid Position")
            return
        if pos == 0:  # Insert at the beginning.
            self.insert_beginning(data)
            return
        if pos == self.size:  # Insert at the end.
            self.insert_end(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(pos):  # Traverse to the desired position.
            current = current.next
        previous = current.prev
        previous.next = new_node
        new_node.prev = previous
        new_node.next = current
        current.prev = new_node
        self.size += 1
        print("Node inserted successfully")

    def delete_beginning(self):
        # Removes the first node from the list.
        if self.is_empty():  # Check if the list is empty.
            print("Linked List is Empty")
            return
        if self.head == self.tail:  # If single node, reset head and tail.
            self.head = None
            self.tail = None
        else:  # Update head and remove its previous link.
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        print("Node deleted successfully")

    def delete_end(self):
        # Removes the last node from the list.
        if self.is_empty():  # Check if the list is empty.
            print("Linked List is Empty")
            return
        if self.head == self.tail:  # If single node, reset head and tail.
            self.head = None
            self.tail = None
        else:  # Update tail and remove its next link.
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        print("Node deleted successfully")

    def delete_position(self, pos):
        # Removes a node at a specific position in the list.
        if pos < 0 or pos >= self.size:  # Validate position.
            print("Invalid Position")
            return
        if pos == 0:  # Delete the first node.
            self.delete_beginning()
            return
        if pos == self.size - 1:  # Delete the last node.
            self.delete_end()
            return
        current = self.head
        for i in range(pos):  # Traverse to the desired position.
            current = current.next
        current.prev.next = current.next  # Link previous to next.
        current.next.prev = current.prev  # Link next to previous.
        self.size -= 1
        print("Node deleted successfully")

    def search(self, element):
        # Searches for an element in the list.
        current = self.head
        position = 0
        while current:  # Traverse and compare each node's data.
            if current.data == element:
                return position  # Return position if found.
            current = current.next
            position += 1
        return -1  # Return -1 if not found.

    def display_forward(self):
        # Displays the list from head to tail.
        if self.is_empty():
            print("Linked List is Empty")
            return
        print(f"Forward Traversal (Size: {self.size})")
        current = self.head
        while current:  # Traverse and print data.
            if current == self.head:
                print(f"[HEAD: {current.data}]", end=" <-> ")
            elif current == self.tail:
                print(f"[TAIL: {current.data}]", end=" <-> ")
            else:
                print(f"[{current.data}]", end=" <-> ")
            current = current.next
        print("None")  # End of list.

    def display_backward(self):
        # Displays the list from tail to head.
        if self.is_empty():
            print("Linked List is Empty")
            return
        print(f"Backward Traversal (Size: {self.size})")
        current = self.tail
        while current:  # Traverse in reverse and print data.
            if current == self.tail:
                print(f"[TAIL: {current.data}]", end=" <-> ")
            elif current == self.head:
                print(f"[HEAD: {current.data}]", end=" <-> ")
            else:
                print(f"[{current.data}]", end=" <-> ")
            current = current.prev
        print("None")  # Start of list.
8

if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("=" * 55)
    print("      DOUBLY LINKED LIST DEMONSTRATION")
    print("=" * 55)

    # Insert Operations
    print("\nInserting Nodes...")

    dll.insert_beginning(20)
    dll.insert_beginning(10)
    dll.insert_end(40)
    dll.insert_end(50)
    dll.insert_position(2, 30)

    print("\nDoubly Linked List (Forward):")
    dll.display_forward()

    print("\nDoubly Linked List (Backward):")
    dll.display_backward()

    # Search Operation
    print("\nSearching for Element 30...")
    position = dll.search(30)

    if position != -1:
        print(f"Element Found at Position {position + 1}")
    else:
        print("Element Not Found")

    # Delete Beginning
    print("\nDeleting First Node...")
    dll.delete_beginning()

    print("\nForward Traversal After Deleting First Node:")
    dll.display_forward()

    # Delete End
    print("\nDeleting Last Node...")
    dll.delete_end()

    print("\nForward Traversal After Deleting Last Node:")
    dll.display_forward()

    # Delete Position
    print("\nDeleting Node at Position 2...")
    dll.delete_position(1)      # Position 2 (0-based index = 1)

    print("\nFinal Doubly Linked List (Forward):")
    dll.display_forward()

    print("\nFinal Doubly Linked List (Backward):")
    dll.display_backward()

    print("\nProgram Executed Successfully.")