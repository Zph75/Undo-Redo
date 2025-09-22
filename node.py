class Node:


    def __init__(self, value):
        # Store the value given when the Node is created
        self.value = value
        # Initialize next pointer as None until linked to another Node
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"