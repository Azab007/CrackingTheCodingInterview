from linked_list import LinkedList, DoublyLinkedList
def sumList(l1,l2):
    p1 = l1.head
    p2 = l2.head
    carry = 0
    res = LinkedList()
    while p1 or p2:
        tmp = carry
        if p1:
            tmp += p1.value
            p1 = p1.next
        if p2:
            tmp+=p2.value
            p2 = p2.next
        sm = tmp % 10
        carry = tmp // 10
        res.add(sm)
    if carry:
        res.add(carry)
    return res

def sumList_ForwardOrder(l1,l2):
    p1 = l1.tail
    p2 = l2.tail
    carry = 0
    res = LinkedList()
    while p1 or p2:
        tmp = carry
        if p1:
            tmp += p1.value
            p1 = p1.prev
        if p2:
            tmp+=p2.value
            p2 = p2.prev
        sm = tmp % 10
        carry = tmp // 10
        res.add_to_beginning(sm)
    if carry:
        res.add_to_beginning(carry)
    return res


if __name__=="__main__":
    l1 = LinkedList.generate(3, 0, 9)
    l2 = LinkedList.generate(2, 0, 9)
    print(l1)
    print(l2)
    res = sumList(l1,l2)
    print(res)
    print("-------------------------------------------")
    l1 = DoublyLinkedList.generate(2, 0, 9)
    l2 = DoublyLinkedList.generate(3, 0, 9)
    print(l1)
    print(l2)
    res = sumList_ForwardOrder(l1,l2)
    print(res)

