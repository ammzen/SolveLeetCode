# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is not None:
            if root.left and root.right:
                ldepth = self.minDepth(root.left)
                rdepth = self.minDepth(root.right)
                return min(ldepth, rdepth) + 1
            elif root.left or root.right:
                return  self.minDepth(root.left) + self.minDepth(root.right) + 1
            else:
                return 1
        return 0
        
if __name__ == '__main__':
    s = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p6 = TreeNode(6)
    p7 = TreeNode(7)
    p1.left = p2
    p2.left = p3
    p2.right = p4
    p3.left = p5
    p5.left = p6
    p6.left = p7
    print s.minDepth(p1)