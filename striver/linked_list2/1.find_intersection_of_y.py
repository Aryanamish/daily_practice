# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def str(self):
        return self.__str__()

    def __str__(self):
        head = self
        ans = ''
        if head is None:
            return ans
        while head:
            ans += f"{head.val}->"
            head = head.next
        return ans[:-2]

    def __repr__(self):
        return self.__str__()


class Solution:
    def reverseList(self, head):
        curr = head.next
        prev = head
        head.next = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            perv = curr
            curr = temp
        head.next = None
        return prev

    def floyd(self, head):
        slow = head
        fast = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        fast = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow

    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        head = self.reverseList(headA)
        headA.next = headB
        # ans = self.floyd(head)
        headA.next = None
        self.reverseList(head)
        return head


def create_list(arr1, arr2):
    headA = ListNode()
    node = headA
    intersection = None
    for num in arr1:
        if isinstance(num, list):
            intersection = ListNode(num[0])
            node.next = intersection
        else:
            node.next = ListNode(num)
        node = node.next
    headB = ListNode()
    node = headB
    for num in arr2:
        if isinstance(num, list):
            node.next = intersection
            break
        node.next = ListNode(num)
        node = node.next
    return [headA.next, headB.next]


if __name__ == '__main__':
    s = Solution()
    headA, headB = create_list([4, 1, [8], 4, 5], [5, 6, 1, [8], 4, 5])
    s.getIntersectionNode(headA, headB)
