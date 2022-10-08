from linked_list import LinkedList
def removeDups(l):
    s = set()
    cur = l.head
    prev = None
    while cur != None:
        if cur.value in s:
            prev.next = cur.next
        else:
            s.add(cur.value)
            prev = cur
        cur=cur.next
    l.tail = prev
    return l

def remove_dups_followup(l):
    runner = current = l.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    l.tail = runner
    return l

if __name__=="__main__":
    l = LinkedList.generate(10, 0, 9)
    print(l)
    removeDups(l)
    print(l)

    l = LinkedList.generate(10, 0, 9)
    print(l)
    remove_dups_followup(l)
    print(l)