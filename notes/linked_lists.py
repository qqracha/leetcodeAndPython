class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # Само значение
        self.next = next # Ссылка на следующий узел

    def __str__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values) + " -> None"
    
    def print_linked_list(head):
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "")
            current = current.next
        print(" -> None")


node3 = ListNode(30)
node2 = ListNode(20, node3) # За 20 идёт node3 
node1 = ListNode(10, node2) # За 10 идёт node2

head = node1



ListNode.print_linked_list(node1)
print(node1)