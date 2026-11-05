# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        vals = []
        
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
                
        preorder(root)
        return " ".join(vals) # Separated by a space

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
            
        # Convert string back to a list of integers in reverse order 
        # so we can efficiently pop() from the end in O(1) time
        vals = [int(x) for x in data.split()][::-1]
        
        def build(lower=float('-inf'), upper=float('inf')) -> Optional[TreeNode]:
            if not vals:
                return None
                
            val = vals[-1]
            # If the next value does not fit within the BST boundaries, 
            # it belongs to another subtree branch
            if val < lower or val > upper:
                return None
                
            vals.pop() # Remove the valid value from our queue
            root = TreeNode(val)
            root.left = build(lower, val)   # Left children must be < val
            root.right = build(val, upper)  # Right children must be > val
            return root
            
        return build()

# Your Codec object will be instantiated and called as such:
# Your codec = Codec()
# codec.deserialize(codec.serialize(root))
