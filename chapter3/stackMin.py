class MinStack():
    def __init__(self):
        self.stack = []        
        self.minvals = []   

    def push(self, value):
        self.stack.append(value)
        if len(self.minvals) == 0 or value <= self.minimum():
            self.minvals.append(value)

    def pop(self):
        value = self.stack.pop()
        if value == self.minimum():
            self.minvals.pop()
        return value

    def minimum(self):
        return self.minvals[-1]

if __name__=="__main__":
    s = MinStack()
    s.push(5)
    s.push(2)
    print(s.minimum())