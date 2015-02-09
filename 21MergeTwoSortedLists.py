# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        tail = head
        while l1 is not None and l2 is not None:
            left = l1.val < l2.val
            tail.next = l1 if left else l2
            tail = tail.next
            l1 = l1.next if left else l1
            l2 = l2 if left else l2.next
        tail.next = l2 if l1 is None else l1
        return head.next

def show(link, n):
    for x in xrange(n):
        try:
            print link.val
        except:
            print 'NoneType'
        else:
            link = link.next


    pass

if __name__ == '__main__':
    s = Solution()
    l11 = ListNode(-9)
    l12 = ListNode(2)
    l11.next = l12
    l12.next = None
    l21 = ListNode(1)
    l22 = ListNode(5)
    l21.next = l22
    show(s.mergeTwoLists(l11, l21), 4)