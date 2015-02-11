# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root:
            differ = self.maxDepth(root.left) - self.maxDepth(root.right)
            if abs(differ) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        return True

    def maxDepth(self, root):
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
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
    p3.right = p6
    p4.left = p7
    print s.isBalanced(p2)