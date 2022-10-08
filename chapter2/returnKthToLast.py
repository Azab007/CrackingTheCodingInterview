from linked_list import LinkedList
def returnKthToLast(l,k):
    size = len(l) - k
    cur = l.head
    for _ in range(size):
        cur=cur.next
    return cur

if __name__=="__main__":
    l = LinkedList.generate(10, 0, 9)
    print(l)
    c = returnKthToLast(l,4)
    print(c.value)