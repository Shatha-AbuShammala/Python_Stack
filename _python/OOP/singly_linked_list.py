class SLNode :
    def __init__(self,val):
        self.value=val
        self.Next= None
class SList :
    def __init__(self):
        self.heade= None

def add_to_front(self,val):
    new_node =SLNode(val)
    new_node.Next = self.head
    self.head= new_node
    return self

def print_values(self):
    runner = self.head
    while runner != None:
        print(runner.value)
        runner = runner.next
    return self

def add_to_back(self, val):
    new_node = SLNode(val)
    if self.head is None:
        self.head = new_node
        return self
    runner = self.head
    while runner.next != None:
        runner = runner.next
    runner.next = new_node
    return self


        