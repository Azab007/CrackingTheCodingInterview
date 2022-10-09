from linked_list import LinkedList
def palindmore(l1):
    slow = fast = l.head
    stack = []
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        tmp = stack.pop()
        if tmp != slow.value:
            return False
        slow = slow.next
    if len(stack) == 0:
        return True
if __name__=="__main__":
    l = LinkedList()
    l.add_multiple([1,2,3,2,1])
    print(l)
    print(palindmore(l))