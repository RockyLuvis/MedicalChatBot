

class node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
    
    def get_length(self,listhead):
    
        nodeobj = listhead
        count = 0
        while (nodeobj):
            #print ("NodeObj val=", nodeobj.val)
            nodeobj = nodeobj.next
            count = count + 1
    
        return count

    def print_nodes(self,listhead):

        nodeobj = listhead
        ll_length = nodeobj.get_length(listhead)
        #print ("ll_length",ll_length)
        while(nodeobj):
            print(f"{nodeobj.val}", end=" -> ")
            nodeobj = nodeobj.next
        print ("None")

    def delete_nodes(self, n, listhead):
        
        nodeobj = listhead
        ll_length = nodeobj.get_length(listhead)
        print ("delete_nodes::ll_length",ll_length)

        #Now goto n-1 position of the node to be removed  and set node.next to node.next.next
        # if ll_lenght = 5, n = then goto ll_length-n , i.e 3
        count = ll_length-n-1 
        #while (count):
        for _ in range(count):
            nodeobj = nodeobj.next
            count = count -1
        #now change the pointer of node.next to node.next.next
        print (f"deleting node: {nodeobj.next.val}")
        nodeobj.next = nodeobj.next.next
        print (f"after deleting node: {nodeobj.val}")

#Takes the node to which val node to be attached
def append(listhead, val):

    listhead1 = node(0)
    #ll_length = listhead1.get_length(listhead)
    
    #print ("DEBUG append :: ll_length= ",ll_length)
    if listhead is None:
        print ("Head cannot be null")
        return False
    
    if (val == None):
        print("ERROR")
        pass
    #Create a new node and append value
    #if (ll_length):
    inode = node(val)
    listhead.next = inode
    
    #listhead1.print_nodes(listhead)
    return listhead



node5 = node(5)
node4=node(4)
node4.next = node5
node3=node(3)
node3.next = node4
node2 = node(2)
node2.next = node3
listhead = node(1)
listhead.next = node2


#len = listhead.get_length(listhead)
#listhead.print_nodes(listhead)
#listhead.delete_nodes(3, listhead)
print("after")
#listhead.print_nodes(listhead)

listhead1 = append(node5, 8)
listhead1 = append(listhead1.next, 10)
listhead1.print_nodes(listhead)