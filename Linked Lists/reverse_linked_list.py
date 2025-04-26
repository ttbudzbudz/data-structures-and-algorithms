class Node:
    """Class representing a node in a singly linked list."""

    def __init__(self, value):
        """
        Initialize a new Node.

        Args:
            value (any): The data value for the node.
        """
        self.value = value
        self.next = None


def reverse_linked_list(head):
    """
    Reverse a singly linked list.

    Args:
        head (Node): The head node of the linked list.

    Returns:
        Node: The new head node of the reversed linked list.
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def print_list(head):
    """
    Print the elements of a linked list.

    Args:
        head (Node): The head node of the linked list.
    """
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Example usage
if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    print("Original linked list:")
    print_list(head)

    # Reverse the linked list
    reversed_head = reverse_linked_list(head)

    print("Reversed linked list:")
    print_list(reversed_head)
