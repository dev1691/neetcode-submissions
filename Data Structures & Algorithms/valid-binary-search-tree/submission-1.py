# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def valid(node,left,right):   
#             if not node:
#                 return True
#             if not(left<node.val<right):
#                 return False
#             return valid(node.left,left,node.val) and valid(node.right,node.val,right)
#         return valid(root,float("-inf"),float("inf"))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Queue will store (node, lower bound, upper bound)
        queue = deque([(root, float('-inf'), float('inf'))])
        
        while queue:
            node, lower, upper = queue.popleft()
            
            # If the current node violates the BST property, return False
            if not (lower < node.val < upper):
                return False
            
            # Add the left child to the queue with updated bounds
            if node.left:
                queue.append((node.left, lower, node.val))
            
            # Add the right child to the queue with updated bounds
            if node.right:
                queue.append((node.right, node.val, upper))
        
        return True      
    
            
