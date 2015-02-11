# -*- coding: utf-8 -*- 

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from collections import deque
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        queue, lists = deque(), []
        queue.append(root)
        while len(queue):
            l = []
            for x in xrange(len(queue)):
                treenode = queue.popleft()
                l.append(treenode.val)
                if treenode.left:
                    queue.append(treenode.left)
                if treenode.right:
                    queue.append(treenode.right)
            lists.append(l)
        return lists

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
    print s.levelOrder(p7)