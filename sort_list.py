
class node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def print_n(nodehead):

    curr = nodehead
    if curr is None:
        print ("nodeHead cannot be Null")
        return False
        
    while(curr):
        print(curr.val, end = '->')
        curr = curr.next
    print (None)
  

    

def sort_list(listhead1, listhead2):

    # Determine longest list and start iteration over short TODO
    # iterate over list head1 , i times
    # innerloop iterated over list head2, j times

    #check listhead2->val [j] is >=listhead1 i and <= i+1 listhaed1 element
    # If yes, create a new node with listhead2->val [j], and assign listhead1->next to newnode(val)->next and change  listhead1->next to newnode
    # and do j++, if listhead2 doesnt fall in between then make take next i node and repeat,, just make sure the remember j value 
    # and start from the next position.
    # Go till end of listhead2 till,, if it is the end then exit from i loop
    i = 0
    j = 0
    current = listhead1

    while (current and current.next):
        if (current.next is not None):
            i_val1 = current.val
            i_val2 = current.next.val
            print ("DEBUG: i_val1, i_val2",i_val1, i_val2)
        else:
            break

        temp = listhead2
        for _ in range(j):
            if (temp is not None):
                print ("DEBUG : Did traverse next val to check is: ",temp.val )
                temp = temp.next

        listhead2 = temp

        #while (listhead2):
        if listhead2 is not None:
            j_val = listhead2.val
            #print ("DEBUG: jval, i_val1, i_val2",j_val,i_val1, i_val2)
            if i_val1 <= j_val <= i_val2:
                #If yes, create a new node with listhead2->val [j]
                insert_node = node(j_val)
                #now insert it in the listhead1
                insert_node.next = current.next
                current.next = insert_node
                j = j+1
                
                print("After insertion:")
                print_n(listhead1)
            else:
                print ("Pick up next i val as j is high")

        i = i+1
        current = current.next
        if current:
            print("Next node to process:", current.val)
        #listhead1 = listhead1.next
        #print("After if:")
        #print_n(listhead1)
        #print ("next Pickup =", listhead1.val)
    
    print("finally::")
    print_n(listhead1)


n2 = node(4)
new_node = node(3)
new_node.next = n2
listhead1 = node(1)
listhead1.next = new_node

n2 = node(4)
new_node = node(2)
new_node.next = n2
listhead2 = node(1)
listhead2.next = new_node

#nobj = node(1)
#nobj.print_n(listhead1)
#nobj.print_n(listhead2)
print_n(listhead1)
print_n(listhead2)

sort_list(listhead1, listhead2)