# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

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
    l1 = ListNode(1)
    l2 = ListNode(1)
    l3 = ListNode(1)
    l4 = ListNode(2)
    l5 = ListNode(2)
    l6 = ListNode(3)
    l7 = ListNode(3)
    l8 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    l7.next = l8
    l8.next = None
    show(s.deleteDuplicates(l1), 4)