# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        # i, j, pre, pre.next = l1, l2, l1, l1
        i, j = l1, l2
        while i and j:
            print i.val, j.val
            i, j = i.next, j.next

        # print l1.val, l1.next
        # l1 = l1.next
        # print l1.val, l1.next
        # l1 = l1.next
            # if i.val < j.val and i.next:
            #     if i.next.val > j.val:
            #         print '1: %d %d' %(i.val, j.val)
            #         pre, i = i, i.next
            #         pre.next = j
            #         pre = j
            #         j = j.next
            #         pre.next = i
            #         # return self.mergeTwoLists(i, j)
            #     else:
            #         print '2: %d %d' %(i.next.val, j.val)
            #         pre, i = i, i.next
            # elif j.val < i.val:
            #     print '3: %d %d' %(i.val, j.val)
            #     pre.next = j
            #     pre = j
            #     pre.next = i
            #     j = j.next
            #     # return self.mergeTwoLists(i, j)
        return l1


if __name__ == '__main__':
    s = Solution()
    l11 = ListNode(1)
    l12 = ListNode(5)
    l13 = ListNode(6)
    l11.next = l12
    l12.next = l13

    
    l2 = ListNode(3)
    p = l2
    p.next = ListNode(4)
    p = p.next
    p.next = ListNode(7)
    p = p.next
    p.next = None
    s.mergeTwoLists(l11, l2)