# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root:
            # ldepth = self.maxDepth(root.left)
            # rdepth = self.maxDepth(root.right)
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return 0

if __name__ == '__main__':
    s = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(2)
    p4 = None
    p5 = TreeNode(3)
    p6 = TreeNode(3)
    p7 = None
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    print s.maxDepth(p6)