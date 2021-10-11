# BST wrapper handles management of node classes 

class node:
    def __init__(self,value=None):
        self.value = value
        self.left_child = None                # left child pointer
        self.right_child = None               # right child pointer

class binary_search_tree:
    def __init__(self):
        self.root = None                        # root null at init

# Insert node function

    def insert(self,value):
        if self.root == None:
            self.root = node(value)               # root of BST
        else:
            self._insert(value,self.root)         # insert node

    def _insert(self, value, cur_node):         
         if value < cur_node.value:               # left child ?
             if cur_node.left_child == None:
                 cur_node.left_child = node(value) 
             else:
                 self._insert(value,cur_node.left_child)   # insert new left child
         elif value > cur_node.value:
             if cur_node.right_child == None:
                 cur_node.right_child=node(value)
             else:
                 self._insert(value,cur_node.right_child)    # insert new right child
         #else:
             #print ("Value already in tree!")

    def print_tree(self):                       # what is in the tree
        if self.root != None:
             print ("Input:")
             self._print_tree(self.root)

    def _print_tree(self,cur_node):
         if cur_node!=None:
             self._print_tree(cur_node.left_child)
             print (str(cur_node.value))
             self._print_tree(cur_node.right_child)

    def height(self):
         if self.root != None:
             return self._height(self.root,0)
         else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height                            # base case

        left_height = self._height(cur_node.left_child,cur_height+1)
        right_height = self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

    def deepest_Node(self,cur_depth):
         if self.root != None:
             return self._deepest_Node(self.root,cur_depth)
         else:
            return 0 

    def _deepest_Node(self,cur_node,cur_depth):
         if cur_node==None: return cur_depth

         if (cur_depth == 1):
                 print("deepest: ", cur_node.value)
                 
         elif (cur_depth > 1):
             left_depth = self._deepest_Node(cur_node.left_child,cur_depth - 1)
             right_depth = self._deepest_Node(cur_node.right_child,cur_depth - 1)
             


def fill_tree(tree,num_elems = 40,max_int = 100):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()
tree = fill_tree(tree)
tree.print_tree()

cur_depth = tree.height()
dn = tree.deepest_Node(cur_depth)
print ("At depth: "+str(cur_depth))

#print ("tree height: "+str(tree.height()))
