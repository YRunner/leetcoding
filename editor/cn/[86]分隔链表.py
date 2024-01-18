
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummpy1 = ListNode(-1)
        dummpy2 = ListNode(-1)
        p = dummpy1
        p1 = dummpy2
        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                p1.next = head
                p1 = p1.next
            temp = head.next
            head.next = None
            head = temp
        p.next = dummpy2.next
        return dummpy1.next



# leetcode submit region end(Prohibit modification and deletion)
