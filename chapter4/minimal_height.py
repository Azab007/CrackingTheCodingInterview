class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.val}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()

def binaryTreeFromArr(arr,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    root = Node(arr[mid])
    root.left = binaryTreeFromArr(arr,start,mid-1)
    root.right = binaryTreeFromArr(arr,mid+1,end)
    return root

if __name__=="__main__":
    arr =[1,2,3,4,5,8,9,11,12,14]
    print(binaryTreeFromArr(arr,0,len(arr)-1))