
class mytree:
    def __init__(self, num, right=None, left=None) -> None:
        self.num = num
        self.right = right
        self.left = left

    #def determine_depth (self,tree,n):
    def determine_depth (self,tree):

        if tree is None:
            return 0      
        #n=n+1
        #ld = self.determine_depth(tree.left,n)
        #rd = self.determine_depth(tree.right,n)
        ld = self.determine_depth(tree.left)
        rd = self.determine_depth(tree.right)
        return max(ld,rd)+1

    def traverse_depth(self, tree, val, depth, n):
        
        if tree is None:
            return False
        
        n = n+1 
        if n == depth:
            #insert the row
            rowLN = mytree(val)
            rowRN = mytree(val)
            rowLN.left = tree.left
            rowLN.right = tree.right
            
            #Now make new node a trees left and right
            tree.left = rowLN
            tree.right = rowRN
        else:

            ld = self.traverse_depth(tree.left, val, depth, n)
            rd = self.traverse_depth(tree.right,val, depth, n)
        return tree
    
    def add_row(self, tree, val, depth):
        try:
            if not tree:
                raise Exception ("Parent tree needed")
            
            #Find the depth of the tree
            # If the total depth of the tree is less than ins_depth then return error
            #Else proceed to insert row
                #If depth == 1, create a tree node and attack whole tree as new_node.left
            if (depth == 1):
                new_node = mytree(val)
                new_node.left = tree
            else:
                #Determine the depth of the  provided tree 
                tree_depth = self.determine_depth(tree)   
                if (depth < tree_depth):
                    # Now store the node at the depth to a temp node
                    Ntree = self.traverse_depth(tree, val, depth, 0)
                else:
                    raise Exception ("Depth to insert row cannot be larger than the tree depth")
            print("Added Row, New Tree {Ntree}")
                        
        except Exception as e:
            raise Exception (e)


def print_tree(root):
    if root is None:
        return
    
    print_tree(root.left)
    print(root.num)
    print_tree(root.right)


root = mytree(3)
root.left = mytree(5)
root.left.right = mytree(1)
root.left.left = mytree(7)

root.right = mytree(6)
root.right.left = mytree(5)

print_tree(root)

td = root.determine_depth(root)
print ("td:",td)

rootobj = mytree(5)
rootobj.add_row(root, 1, 2)
print_tree(root)