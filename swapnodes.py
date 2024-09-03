'''
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
'''
import sys
from collections import deque

class node:
    stack = deque()

    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
    
    def print_n(self, headnode):
        curr = headnode
        i=0
        while (curr):
            #Traverse the list
            print(curr.val, end = "->")
            curr = curr.next
            i = i+1
        print("None")
        print ("num of nodes = i", i)

    def swapnodes(self, headnode):

        curr = headnode
        head = curr.next
        p = None
        #while curr is not None
        while (curr):
            
            first = curr
            second = curr.next             

            #assign new node to curr 
            first.next = second.next
            second.next = first

            if p:
                p.next = second
            p = first
            #point curr to next.next
            curr = first.next

            # make the headnode to temp only for the first node. 
            #        
        self.print_n (head)

    def get_length(self, headnode):
        i = 0
        if (headnode is None):
            return 0
        
        curr = headnode
        while (curr):
            i = i+1
            curr = curr.next #Traverse till end
        
        #print("num of nodes:", i)
        return i

    def chunk_revesal(self, headnode, k):

        curr = headnode
        new_head = node(0)
        prev = new_head
        #new_head_flag = False
        try:

            if k <= 0:
                raise ValueError ("Chunk size has to be greater than 0")

            #get length of list
            if headnode is None or headnode.next is None or k == 1 :
                return headnode
            else:
                #Get length of the list
                list_len = self.get_length(headnode)

            # determining chunks, if list len is multiple of k then reverse till end
            # if listlen is not multiple then leave last less than k number of node unreversed
            #if list_len % k == 0:
            num_chunks = list_len // k

            #Traverse till the first Kth chunk node
            for _ in range(num_chunks):

                if (curr):

                    for _ in range(k):
                        #Push curr.next to LIFO
                        self.stack.append(curr)
                        curr = curr.next

                    #   Now curr.next is pointing to the next chunk
                    # Make curr.next point to first.next
                    # This is for 3 node reversal case
                    while (self.stack):
                        prev.next = self.stack.pop()
                        #if new_head_flag == 0:  # First chunk reversal
                        #    new_head = prev.next
                        #    new_head_flag = True
                        prev = prev.next

                prev.next = curr


            remaining_nodes = list_len - (k* num_chunks)
            if ( remaining_nodes > 0):
                #attach remaining nodes
                prev.next = curr
        
        except Exception as e:
            print (e)
            return headnode

        return new_head 


n4 = node(4)
n3 = node(3)
n3.next = n4
n2 = node(2)
n2.next = n3
headnode = node(1)
headnode.next = n2

headnode.print_n(headnode)
#headnode.swapnodes(headnode)
new_head = headnode.chunk_revesal(headnode,0)
headnode.print_n(new_head.next)