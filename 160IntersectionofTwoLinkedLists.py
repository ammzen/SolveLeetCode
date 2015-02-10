# -*- coding: utf-8 -*- 
# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        i, j, lenA, lenB = headA, headB, 0, 0
        while i and j:
            i, j = i.next, j.next
        ii, jj = headA, headB
        while i:
            i, ii = i.next, ii.next
        while j:
            j, jj = j.next, jj.next
        while ii != jj:
            ii, jj = ii.next, jj.next
        return ii

        # while i:
        #     lenA += 1
        #     i = i.next
        # while j:
        #     lenB += 1
        #     j = j.next
        # i, j = headA, headB
        # if lenA > lenB:
        #     for x in xrange(lenA - lenB):
        #         i = i.next
        # else:
        #     for x in xrange(lenB - lenA):
        #         j = j.next
        # while i != j:
        #     i, j = i.next, j.next
        # return i

def show(link, n):
    for x in xrange(n):
        try:
            print link.val
        except:
            print 'NoneType'
        else:
            link = link.next

if __name__ == '__main__':
    s = Solution()
    l11 = ListNode('a1')
    l12 = ListNode('a2')
    l13 = ListNode('c1')
    l14 = ListNode('c2')
    l15 = ListNode('c3')
    l11.next = l12
    l12.next = l13
    l13.next = l14
    l14.next = l15
    l15.next = None

    l21 = ListNode('b1')
    l22 = ListNode('b2')
    l23 = ListNode('b3')
    l24 = l13
    l25 = l14
    l26 = l15
    l21.next = l22
    l22.next = l23
    l23.next = l24
    l24.next = l25
    l25.next = l26
    l26.next = None
    print s.getIntersectionNode(l11, l21).val
