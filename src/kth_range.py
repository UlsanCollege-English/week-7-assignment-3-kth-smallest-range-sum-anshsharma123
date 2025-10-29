class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    """
    Recursively inserts a key into the BST and returns the new root.
    If the key already exists, it rejects the duplicate and returns the original root.
    """
    # Base case: If the tree (or subtree) is empty, create a new node
    if root is None:
        return Node(key)

    # Recursive step
    if key == root.key:
        return root  # Reject duplicate, return unchanged root
    elif key < root.key:
        # Insert into the left subtree and update the left child
        root.left = insert(root.left, key)
    else: # key > root.key
        # Insert into the right subtree and update the right child
        root.right = insert(root.right, key)
    
    # Return the (possibly modified) root node
    return root

def kth_smallest(root, k):
    """
    Finds the k-th smallest element in the BST (1-indexed).
    Uses an iterative in-order traversal.
    Raises IndexError if k is out of bounds.
    """
    # Stack for iterative in-order traversal
    stack = []
    count = 0
    cur = root

    while cur or stack:
        # 1. Go as far left as possible
        while cur:
            stack.append(cur)
            cur = cur.left
        
        # 2. Visit the node (pop from stack)
        cur = stack.pop()
        count += 1
        
        # 3. Check if this is the k-th node
        if count == k:
            return cur.key
            
        # 4. Go to the right subtree
        cur = cur.right
    
    # If we finish the loop without returning, k was larger than the node count
    raise IndexError("k is out of bounds for the tree size")

def range_sum_bst(root, low, high):
    """
    Calculates the sum of all node keys within the range [low, high] (inclusive).
    Uses a recursive traversal with BST pruning.
    """
    # Base case
    if root is None:
        return 0
    
    current_sum = 0
    
    # 1. Check if the current node's key is in the range
    if low <= root.key <= high:
        current_sum += root.key
        
    # 2. Recurse left ONLY if the current key is greater than the low bound
    # (If root.key <= low, nothing to the left can be in range)
    if root.key > low:
        current_sum += range_sum_bst(root.left, low, high)
    
    # 3. Recurse right ONLY if the current key is less than the high bound
    # (If root.key >= high, nothing to the right can be in range)
    if root.key < high:
        current_sum += range_sum_bst(root.right, low, high)
        
    return current_sum