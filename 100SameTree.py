# Given two binary trees, write a function to check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)    
    p.right = TreeNode(3)
    p = TreeNode(2)
    p.left = TreeNode(4)    
    p.right = None
    p = TreeNode(3)
    p.left = None    
    p.right = TreeNode(5)
    p = TreeNode(4)
    p.left = None    
    p.right = None
    p = TreeNode(5)
    p.left = None    
    p.right = None
    q = TreeNode(1)
    p = TreeNode(1)
    print s.isSameTree(q,p)


