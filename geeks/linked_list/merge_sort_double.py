#User function Template for python3
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''


#Function to sort the given doubly linked list using Merge Sort.
def merge(head1, head2):
    if head1 is not None and head2 is not None:
        if head1.data < head2.data:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next

        curr = head
        while head1 is not None and head2 is not None:
            if head1.data < head2.data:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next

            curr.next.prev = curr
            curr = curr.next

        while head1 is not None:
            curr.next = head1
            head1 = head1.next
            curr.next.prev = curr
            curr = curr.next
        while head2 is not None:
            curr.next = head2
            head2 = head2.next
            curr.next.prev = curr
            curr = curr.next
        return head
    return None


def sortDoubly(head):
    if head is not None and head.next is not None:
        slow = head
        fast = head.next
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
        head2 = slow.next
        slow.next = None
        head2.prev = None
        head = sortDoubly(head)
        head2 = sortDoubly(head2)
        return merge(head, head2)

    return head


#{
# Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        llist.head = sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends