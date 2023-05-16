class Queue:

    def __init__(self,size):
        self.n = size
        self.lst = [None]*self.n

    def is_empty(self):
        count = sum([1 for i in self.lst if i == None])
        if count == self.n: return True
        else: return False
    
    def is_full(self):
        count = len([1 for i in self.lst if i == None])
        if count == 0: return True
        else: return False

    def enqueue(self,val):
        if not self.is_full():
            self.lst.append(val)
            self.lst.remove(None)
        else: print("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            self.lst.remove([i for i in self.lst if i != None][0])
            self.lst.append(None)
        else: print("Queue is empty")


    def __str__(self):
        try:
            a = ",".join([str(i) for i in self.lst if i != None])
            return f"Queue: {a}\nFront: {a[0]}\nBack: {a[len(a)-1]}"
        except IndexError:
            return "Queue is empty"


if __name__ == "__main__":
    x = Queue(20)
    x.enqueue(2)
    x.enqueue(5)
    x.enqueue(6)
    x.dequeue()
    x.dequeue()
    print(x)
