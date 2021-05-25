class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            # go till end
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def traverse(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

    def delete(self, val):
        if self.head == None:
            return -1
        # only one node
        if self.head.data == val:
            self.head = self.head.next
        # more than one node
        else:
            cur = self.head
            prev = None
            while cur != None:
                if cur.data == val:
                    break
                prev = cur
                cur = cur.next
            # number does not exists in ll
            if cur == None:
                return -1
            prev.next = cur.next


ll = LinkedList()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.traverse()
ll.delete(1)
ll.traverse()