


class Node:

    def __init__(self,value,pointer):
        self.val = value
        self.next = pointer
        


class LinkedList:

    def __init__(self,head):
        self.head = head
        self.mem = {0:self.head}
        self.mem.update({i:None for i in range(1,16)})
        self.last = self.head

    def __str__(self):
        return ",".join([f"({j.val},{j.next})" for i,j in self.mem.items() if j != None])
    
    def __add__(self, node):
        self.mem[self.last.next] = node
        self.last = node

    def __sub__(self,node):
        mem_loc = next((i for i,j in self.mem.items() if j == node),None)
        self.mem[mem_loc] = None if mem_loc != None else print("Cant delete that value")

if __name__ == "__main__":
    nums = LinkedList(Node(2,4))
    print(nums.mem)
    nums + Node(1,5)

    #print(nums.mem)