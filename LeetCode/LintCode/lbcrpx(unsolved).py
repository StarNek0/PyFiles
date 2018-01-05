# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/18 16:07'

"""
链表插入排序
Given 1->3->2->0->null, return 0->1->2->3->null
"""

"""
Definition of ListNode"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        cur = dummy = ListNode(0)
        while head:
            if cur and cur.val > head.val:  # reset pointer only when new number is smaller than pointer value
                cur = dummy
            while cur.next and cur.next.val < head.val:  # classic insertion sort to find position
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next  # insert
        return dummy.next
# this is the solution from leetcode 汗。。。看不懂
if __name__ == '__main__':
    so = Solution()
    so.insertionSortList(ListNode(0))
    so.insertionSortList(ListNode(1))
