from linked_list import LinkedList
def deleteMiddleNode(n):
    n.value = n.next.value
    n.next = n.next.next
    

if __name__=="__main__":
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8, 9])
    print(ll)
    deleteMiddleNode(middle_node)
    print(ll)