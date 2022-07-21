"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #if tree is empty return empty list
        if root is None:
            return []
        
        #initialize stack with first root node
        stack, output = [root, ], []            
        
        #while the stack is not empty explore the elements on the stack and append each value to the output array
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
                
        return output
