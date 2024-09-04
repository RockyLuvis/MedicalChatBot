# Declare a Tree Node class 

class TreeNode :
    def __init__(self, value, left= None, right= None) -> None:
        self.left = left
        self.right = right
        self.value = value

def merge_tree(t1: TreeNode, t2: TreeNode):

    if (t1 is None and t2 is None):
        return None
    if (t1 is None):
        return t2
    if (t2 is None):
        return t1
    else:
        merge = TreeNode(t1.value + t2.value)

        merge.left = merge_tree(t1.left, t2.left)
        merge.right = merge_tree(t1.right, t2.right)
        return merge

def print_tree(merge):
    
    if merge is None:
        return 
    print_tree(merge.left)
    print(merge.value)
    print_tree(merge.right)

def inorderBST (merge):
    
    if merge is None:
        return 
    inorderBST(merge.left)
    sort_list.append(merge.value)
    inorderBST(merge.right)
    return sort_list

def createBalTree( sort_list ):
    
    if not sort_list:
        return None
   
    #Get the middle number in the list
    m = len(sort_list)//2
    mid = sort_list[m]

    #print ("DEBUG: mid=", mid)

    #create a node
    bst = TreeNode(mid)
    bst.left = createBalTree(sort_list[:m])
    bst.right = createBalTree(sort_list[m+1:])
    return bst

def findheight (merge):
    
    if merge is None:
        return 0
    
    ltht = findheight(merge.left)
    rtht = findheight(merge.right)
    return 1+max(ltht, rtht)

Tree1 = TreeNode(2)
Tree1.left = TreeNode(3)
Tree1.right = TreeNode(4)
Tree1.left.left = TreeNode(6)

Tree2 = TreeNode(2)
Tree2.left = TreeNode(3)
Tree2.right = TreeNode(4)
Tree2.right.right = TreeNode(5)

merge = merge_tree(Tree1, Tree2)

sort_list = []
#sort_list = print_tree(merge)
#print(sorted(sort_list, reverse=True))
sort_list = inorderBST(merge)
print ("sort_list", sort_list)
bst = createBalTree(sort_list)
print_tree(bst)