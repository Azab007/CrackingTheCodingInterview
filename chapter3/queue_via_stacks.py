class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    def enQueue(self, x):
        self.s1.append(x)
 
    def deQueue(self):
 
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is Empty")
            return
 
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                tmp = self.s1.pop()
                self.s2.append(tmp)
            return self.s2.pop()
 
        else:
            return self.s2.pop()
 
    # Driver code
if __name__ == '__main__':
    q = MyQueue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())