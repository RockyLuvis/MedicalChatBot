#Fixed size array or list

# Maintain 2 pointer - Front and rare
# When Deque happens the front points the next element and no element shifting happens
# so when deque happens and front is point to the next highest element,, 
# the top of the array 0th index is empty (None),, and when rear reaches end of the array 
# i.e rare==len(array), then code has to start the 0th index for open slots?

class mycircularqueue:
    def __init__(self, qsize) -> None:
        #initialize Queue
        self.front = -1
        self.rear = -1
        self.size = qsize
        self.myqueue = [None] * qsize


    def get_front(self):   
        return self.front

    def get_rear(self):
        return self.rear

    def isEmpty(self):
        #check if queue is empty
        if (self.front == -1):
            return True
        else:
            return False
    
    def isFull(self):
        if ((self.rear + 1) % self.size == self.front):
            return True


    def enQueue(self, num):
        #check if queue is empty
        if (self.isEmpty()):
            self.front = 0 #index poinitng to the front of the queue
            #self.rear = 0 #index poininting to the rear of the queue
            self.rear = (self.rear + 1)% self.size
            self.myqueue[self.rear] = num
            print ("Enqueued empty q", self.myqueue)
        else:
            # Get the rear of the list
            if (self.isFull()):
                print ("Queue Full")
                return False
            else:
                self.rear = (self.rear + 1)% self.size
                self.myqueue[self.rear] = num
                print ("Enqueued, self.rear ", self.myqueue, self.rear )
                return True
                        #append the num to the list

    def deQueue(self):
        #if queue is empty return -1
        if (self.isEmpty()):    
            print ("Dequeue faield empty Queue ")
            return False
        
        else:
            #Get the index of element pointing to the top of the queue
            qfront_index = self.get_front()

            #Get the value from the qfront_index
            deq_num = self.myqueue[qfront_index]
            
            if (self.front == self.rear):
                #queue is empty
                self.front = -1
                self.rear = -1
            else:
                self.myqueue[qfront_index] = None
                self.front = (self.front+1) % self.size

            return deq_num

mycircularqueueObj = mycircularqueue(3)
#front = mycircularqueueObj.get_rear()
mycircularqueueObj.enQueue(10)
front = mycircularqueueObj.get_rear()
print ("rear1", front)
mycircularqueueObj.enQueue(20)

front = mycircularqueueObj.get_rear()
print ("rear2", front)
mycircularqueueObj.enQueue(30)

front = mycircularqueueObj.get_front()
print ("front", front)
#mycircularqueueObj.deQueue()
mycircularqueueObj.enQueue(40)

front = mycircularqueueObj.get_rear()
print ("rear4", front)

