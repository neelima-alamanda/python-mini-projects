class Node:
    # Node class represents each element (node) in the linked list.
    def __init__(self, data):
        self.data = data   # Value of the node.
        self.next = None   # Pointer to the next node in the linked list.

class LinkedList:
    # Class to implement a singly linked list with head, tail, and size.
    def __init__(self):
        self.head = None  # Pointer to the first node in the list.
        self.tail = None  # Pointer to the last node in the list.
        self.size = 0     # Keeps track of the size of the list.

    def is_empty(self):
        # Returns True if the list is empty, otherwise False.
        return self.size == 0

    def insert_beginning(self, data):
        # Inserts a new node with 'data' at the beginning of the list.
        front_node = Node(data)

        if self.is_empty():  # If the list is empty, update both head and tail.
            self.head = front_node
            self.tail = front_node
        else:                # Otherwise, update head to the new node.
            front_node.next = self.head
            self.head = front_node

        self.size += 1       # Update size of the list.
        print("Node inserted successfully")

    def insert_end(self, data):
        # Inserts a new node with 'data' at the end of the list.
        end_node = Node(data)

        if self.is_empty():  # If the list is empty, it becomes both head and tail.
            self.head = end_node
            self.tail = end_node
        else:                # Append the new node to the current tail.
            self.tail.next = end_node
            self.tail = end_node

        self.size += 1       # Update the list size.
        print("Node inserted successfully")

    def insert_position(self, pos, data):
        # Inserts a new node with 'data' at the specified position.
        if pos < 0 or pos > self.size:  # Check for invalid position.
            print("Invalid Position")
            return

        new_node = Node(data)
        if pos == 0:  # Insert at the beginning of the list.
            new_node.next = self.head
            self.head = new_node
        else:          # Traverse to the position and insert.
            current = self.head
            for i in range(pos - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        if new_node.next is None:  # Update the tail if inserted at the end.
            self.tail = new_node

        self.size += 1  # Update size of the list.
        print("Node inserted successfully")

    def delete_beginning(self):
        # Deletes the first node in the list.
        if self.is_empty():  # Check if the list is empty.
            print("Linked list is empty")
            return

        if self.head == self.tail:  # If only one node, reset head and tail.
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next  # Shift head to the next node.

        self.size -= 1  # Reduce the size of the list.
        print("Node deleted successfully")

    def delete_end(self):
        # Deletes the last node in the list.
        if self.is_empty():  # If list is empty, no deletion possible.
            print("Linked list is empty")
            return

        if self.head.next is None:  # If only one node, reset head and tail.
            self.head = None
            self.tail = None
        else:                       # Traverse to the second-to-last node.
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None     # Remove the last node.
            self.tail = current     # Update the tail.

        self.size -= 1  # Reduce the size of the list.
        print("Node deleted successfully")

    def delete_position(self, pos):
        # Deletes the node at the specified position.
        if pos < 0 or pos >= self.size:  # Check for invalid position.
            print("Invalid Position")
            return

        if pos == 0:  # Delete the first node.
            if self.head == self.tail:  # If only one node, reset head and tail.
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next  # Update head to the next node.
            self.size -= 1
            print("Node deleted successfully")
            return

        current = self.head
        for i in range(pos - 1):  # Traverse to the preceding node.
            current = current.next
        
        deleted_node = current.next      # Node to be deleted.
        current.next = deleted_node.next # Remove the node by skipping it.

        if current.next is None:  # If last node is deleted, update tail.
            self.tail = current

        self.size -= 1  # Reduce the size of the list.
        print("Node deleted successfully")

    def search(self, element):
        # Searches for the element in the list and returns its position.
        current = self.head
        position = 0

        while current:  # Traverse through the list.
            if current.data == element:  # If element found, return position.
                return position
            current = current.next
            position += 1

        return -1  # Return -1 if element is not found.

    def display(self):
        # Displays the linked list elements and other useful information.
        if self.is_empty():  # Check if list is empty.
            print("Linked List is Empty")
            return

        print(f"Linked List (size: {self.size}):")  # Print size.
        current = self.head

        while current:  # Traverse and print all nodes.
            if current == self.head:
                print(f"[HEAD: {current.data}]", end=" -> ")
            elif current == self.tail:
                print(f"[TAIL: {current.data}]", end=" -> ")
            else:
                print(f"[{current.data}]", end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list.

if __name__ == "__main__":
    ll = LinkedList()

    print("=" * 50)
    print("       SINGLY LINKED LIST DEMONSTRATION")
    print("=" * 50)

    # Insert Operations
    print("\nInserting Nodes...")

    ll.insert_beginning(20)
    ll.insert_beginning(10)
    ll.insert_end(40)
    ll.insert_end(50)
    ll.insert_position(2, 30)

    print("\nLinked List after Insert Operations:")
    ll.display()

    # Search Operation
    print("\nSearching for Element 30...")
    position = ll.search(30)

    if position != -1:
        print(f"Element Found at Position {position + 1}")
    else:
        print("Element Not Found")

    # Delete Beginning
    print("\nDeleting First Node...")
    ll.delete_beginning()
    ll.display()

    # Delete End
    print("\nDeleting Last Node...")
    ll.delete_end()
    ll.display()

    # Delete Position
    print("\nDeleting Node at Position 2...")
    ll.delete_position(1)      # Position 2 (0-based index = 1)
    ll.display()

    print("\nProgram Executed Successfully.")