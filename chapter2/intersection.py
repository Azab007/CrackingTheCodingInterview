from linked_list import LinkedList
def intersection_withSet(l1,l2):
    s = set()
    p1 = l1.head
    p2 = l2.head
    while p1:
        s.add(p1)
        p1=p1.next
    while p2:
        if p2 in s:
            return p2
        p2 = p2.next
    return False

def intersection(l1,l2):
    if l1.tail != l2.tail:
        return False
    l1_len,l2_len = len(l1),len(l2)
    p1,p2 = l1.head,l2.head
    diff = abs(l1_len - l2_len)
    if l1_len > l2_len:
        for _ in range(diff):
            p1=p1.next
    else:
        for _ in range(diff):
            p2=p2.next
    while p1:
        if p1 == p2:
            return p1
        p1=p1.next
        p2=p2.next
    return False
    
if __name__=="__main__":
    l1 = LinkedList.generate(4,0,9)
    l2 = LinkedList.generate(4,0,9)
    l2.tail.next = l1.head
    l2.tail = l1.tail
    print(l1)
    print(l2)
    print(intersection(l1,l2))