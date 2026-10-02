class LinkedList:
    class clsNode:
        def __init__(self, value):
            self.next = None
            self.previous = None
            self.value = value

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_head(self, value):
        new_node = self.clsNode(value=value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.size += 1
        return new_node

    def pop_tail(self):
        if self.tail == None:
            return
        removed_value = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return removed_value
        self.tail = self.tail.previous
        self.tail.next = None
        self.size -= 1
        return removed_value
