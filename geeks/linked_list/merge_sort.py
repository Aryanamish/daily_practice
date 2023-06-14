#User function Template for python3
'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''


class Solution:
    #Function to sort the given linked list using Merge Sort.
    def merge(self, head1, head2):

        if head1 is not None and head2 is not None:
            if head1.data < head2.data:
                new_head = head1
                head1 = head1.next
            else:
                new_head = head2
                head2 = head2.next
            rv = new_head
            while head1 is not None and head2 is not None:
                if head1.data < head2.data:
                    new_head.next = head1
                    head1 = head1.next
                else:
                    new_head.next = head2
                    head2 = head2.next
                new_head = new_head.next
            while head1 is not None:
                new_head.next = head1
                head1 = head1.next
                new_head = new_head.next
            while head2 is not None:
                new_head.next = head2
                head2 = head2.next
                new_head = new_head.next
            return rv

    def mergeSort(self, head):
        if head is not None and head.next is not None:

            fast = head.next
            slow = head
            mid = 1
            while fast is not None:
                mid += 1
                fast = fast.next
                if fast is not None:
                    fast = fast.next
                    slow = slow.next
            head2 = slow.next
            slow.next = None

            head = self.mergeSort(head)
            head2 = self.mergeSort(head2)
            return self.merge(head, head2)
        return head


class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList()  # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends