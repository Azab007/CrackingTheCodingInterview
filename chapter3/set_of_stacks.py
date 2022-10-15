class Set_of_stacks:
    def __init__(self,c):
        self.__capacity = c
        self.__stacks = []
        self.__curCapacity = 0
        self.__index = -1
    def push(self,val):
        if self.__curCapacity == self.__capacity or self.__index==-1:
            self.__Exceeded_push(val)
        else:
            self.__stacks[self.__index].append(val)
            self.__curCapacity+=1
    def pop(self):
        if self.__index == -1:
            raise Exception("list is empty")
        if self.__curCapacity == 0:
            return self.__Exceeded_pop()
        else:
            self.__curCapacity-=1
            return self.__stacks[self.__index].pop()
            
    def peek(self):
        return self.__stacks[self.__index][-1]
    def popAt(self,i):
        return self.leftShift(i)

    def leftShift(self,i):
        if i == self.__index:
            return self.pop()
        elif i < self.__index:
            res = self.__stacks[i].pop()
            while i < self.__index:
                tmp = self.__stacks[i+1].pop(0)
                self.__stacks[i].append(tmp)
                i+=1
            self.__curCapacity-=1
            if self.__curCapacity == 0:
                self.__stacks.pop()
                self.__index-=1
                self.__curCapacity=self.__capacity
            return res
        else:
            raise Exception("List index out of range")

    
    def __Exceeded_push(self,val):
        new = []
        new.append(val)
        self.__stacks.append(new)
        self.__index+=1
        self.__curCapacity=1

    def __Exceeded_pop(self):
        self.__stacks.pop()
        self.__index-=1
        self.__curCapacity=self.__capacity-1
        return self.__stacks[self.__index].pop()

if __name__=="__main__":
    s = Set_of_stacks(2)
    s.push(10)
    s.push(20)
    s.push(30)
    #print(s.__stacks)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    #print(s.__stacks)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    print(s.popAt(0))
    print(s.pop())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    #print(s.__stacks)

