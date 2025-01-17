class Queue:
    def __init__(self):
        self.value=[]
    def enqueue(self,x):
        self.value.append(x)    
    def dequeue(self):
        if(self.value==[]):
            return "Queue is Empty"    
        front=self.value[0]
        self.value=self.value[1:]
        return front
    def get_rare(self):
        rare=self.value[-1]
        return rare
    def Size(self):
        return len(self.value)
q=Queue()    
a=int(input("Enter limit"))
for i in range (a):
    v=int(input("Enter number"))
    q.enqueue(v)
print(q.value)   
print(q.dequeue()) 
print(q.Size())
print(q.get_rare())
