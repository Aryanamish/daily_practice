# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        l = [self.val]
        n = self.next
        while n is not None:
            l.append(n.val)
            n = n.next
        return str(l)

    def __repr__(self):
        return self.__str__()
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = l1
        list2 = l2
        num1 = [str(list1.val)]
        num2 = [str(list2.val)]
        while list1.next is not None:
            list1 = list1.next
            num1.append(str(list1.val))
        
        while list2.next is not None:
            list2 = list2.next
            num2.append(str(list2.val))

        num1.reverse()
        num2.reverse()
        num1 = int(''.join(num1))
        num2 = int(''.join(num2))
        print(num1)
        print(num2)
        num3 = num1 + num2
        print(num3)
        return self.create_linked_list(num3)
        
    def create_linked_list(self, integer):
        linked_list = ListNode(val=integer % 10)
        integer = int((integer - integer % 10)/10)
        if integer == 0:
            return linked_list
        next_node = ListNode()
        linked_list.next = next_node
        
        while integer != 0:
            last_digit = integer % 10
            next_node.val = last_digit
            integer = int((integer - last_digit)/10)
            if integer != 0:
                next_node.next = ListNode()
                next_node = next_node.next
                
        return linked_list
s = Solution()
l1 = ListNode(val=0)
l2 = ListNode(val=0)

print(s.addTwoNumbers(l1, l2))


o(N)
a = [[1, 'simpy'], [2, 'dimpy']]

o(1)
a = {'simpy':1, 'dimpy':2}