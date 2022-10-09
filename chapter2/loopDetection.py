from linked_list import LinkedList
def loopDectection(l):
    s =set()
    p = l.head
    while p:
        if p in s:
            return True, p
        s.add(p)
        p=p.next
    return False, ''
if __name__=="__main__":
    l1 = LinkedList.generate(5,0,9)
    l1.tail.next = l1.head.next
    #print(l1)
    print(loopDectection(l1))