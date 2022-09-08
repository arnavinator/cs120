#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
from multiprocessing.sharedctypes import Value


class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)

# return the size of each child
def calculate_sizes(v):
    # default values for size of left and right children
    left_size = 0
    right_size = 0
    
    # if left or right children, need to include their size for current node
    if (v.left is not None):
        left_size = calculate_sizes(v.left)
    if (v.right is not None):
        right_size = calculate_sizes(v.right)
    
    # total size for the current node if left_size + right_size + size of self
    v.size = left_size + right_size + 1
    return v.size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 
    n2 = r.size / 2
    # iterate without bound since we know the desired vertex must exist
    while (True):
        rl = False
        rr = False
        if (r.left is not None):
            rl = True
        if (r.right is not None):
            rr = True
        if (rl and rr):  
            # if 2 children subtrees exist, this is the case we desire
            if (r.left.size <= n2 and r.right.size <= n2):
                return r
            
            # if not found, then traverse one layer deeper (to larger size subtree)
            else:
                if (r.left.size >= r.right.size):
                    r = r.left
                else:
                    r = r.right
        elif (rl):
            # if 1 child subtree exists, this is one case we desire
            if (r.left.size <= n2):
                return r
            else:
                r = r.left
        elif (rr):
            # if 1 child subtree exists, this is the other case we desire
            if (r.right.size <= n2):
                return r
            else:
                r = r.right
        if (not rl and not rr):
            # if we have reached the child node, then this must be the node to remove!
            return r
