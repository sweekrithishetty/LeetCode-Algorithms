#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
            
        depth = 0
        q = []
        q.append(root)
        
        while q:
            depth += 1
            temp = []
            
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
        return depth
      
 #Approach: Depth first search
class Solution(object):
    def maxDepth(self,root):
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if l > r:
            return l + 1
        return r + 1
