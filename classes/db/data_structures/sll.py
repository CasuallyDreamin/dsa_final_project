class sll:
    def __init__(self):
        self.head: sll_node = None
    
    def add_first(self, data):
        new_node = sll_node(data)
        new_node.next = self.head
        self.head = new_node

    def __repr__(self):
        rpr = self.head.__repr__()
        
        if self.head:
            curr = self.head.next
            while curr:
                rpr = rpr + "->" + str(curr)
                curr = curr.next
        else: rpr = "Empty"
        return rpr


class sll_node:
    def __init__(self, data):
        self.data = data
        self.next: sll_node = None

    def __repr__(self):
        return f"({self.data})"