#Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
  
Inorder : Left to Right pattern


  
#Approach 1: Recursion - root to node
class Solution(object):
    def inorderTraversal(self, root):
       if root is None:
        return []
       return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
#Approach 2:Stack - node to root
class Solution:
    def inorderTraversal(self, root):
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
     
