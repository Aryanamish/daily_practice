# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def list_to_node(l):
        node = rv = ListNode()
        prev = None
        for i in l:
            node.val = i
            node.next = ListNode()
            prev = node
            node = node.next
        prev.next = None
        return rv

    def print(self):
        node = self
        print('[', end='')
        while node is not None:
            print(node.val, end=' ')
            node = node.next
        print(']')

class Solution:
    def mergeTwoLists(self, l1, l2):
        new_list = ListNode(0, None)
        node = new_list
        while l1 is not None and l2 is not None:
            val1, val2 = l1.val, l2.val
            if val1 < val2:
                node.next = ListNode(val1)
                l1 = l1.next
            else:
                node.next = ListNode(val2)
                l2 = l2.next

            node = node.next

        while l1 is not None:
            node.next = ListNode(l1.val)
            l1 = l1.next
            node = node.next
        
        while l2 is not None:
            node.next = ListNode(l2.val)
            l2 = l2.next
            node = node.next
        
        return new_list.next


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode.list_to_node([1,2,4])
    l2 = ListNode.list_to_node([1,3,4])
    s.mergeTwoLists(l1,l2).print()
