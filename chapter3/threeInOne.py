class multipleStack:
    def __init__(self,num_of_stacks,stack_size):
        self.num_of_stacks = num_of_stacks
        self.stack_size = stack_size
        self.arr = [0]* (num_of_stacks*stack_size)
        self.sizes = [0]*num_of_stacks
    def push(self,val,stack_num):
        if self.is_full(stack_num):
            raise Exception("stack is full")
        self.sizes[stack_num]+=1
        self.arr[self.top_index(stack_num)] = val
    def pop(self,stack_num):
        if self.is_empty(stack_num):
            raise Exception("stack is empty")
        val = self.arr[self.top_index(stack_num)]
        self.arr[self.top_index(stack_num)] = 0
        self.sizes[stack_num]-=1
        return val
    def peek(self,stack_num):
        return self.arr[self.top_index(stack_num)]
    def is_empty(self,stack_num):
        return self.sizes[stack_num] == 0
    def is_full(self,stack_num):
        return self.sizes[stack_num] == self.stack_size
    def top_index(self,stack_num):
        begin = stack_num*self.stack_size
        return begin + self.sizes[stack_num]-1
if __name__=="__main__":
    ss = multipleStack(2,3)
    ss.push(5,0)
    ss.push(7,0)
    ss.push(6,1)
    print(ss.pop(0))
    print(ss.pop(0))
    print(ss.pop(0))