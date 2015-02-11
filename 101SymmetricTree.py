# -*- coding: utf-8 -*- 

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is not None:
            if not isTreeSym(root.left, root.right):
                return False
        return True

def isTreeSym(p, q):
    if p == None and q == None:
        return True
    elif p and q:
        return p.val == q.val and isTreeSym(p.left, q.right) and isTreeSym(p.right, q.left)
    else:
        return False

if __name__ == '__main__':
    s = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(2)
    p4 = None
    p5 = TreeNode(3)
    p6 = None
    p7 = TreeNode(3)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    print s.isSymmetric(p1)
        