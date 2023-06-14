#User function Template for python3
'''
Function Arguments :
		@param  : head (given head of linked list), k(value of k)
		@return : None, Just swap the nodes
		
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''


#Function to swap Kth node from beginning and end in a linked list.
def swapkthnode(head, n, k):
    if n % 2 == 1 and (n - k + 1 == k):
        pass
    elif k == 1 or n == k:
        tail = None
        curr = head.next
        prev = head

        while curr.next is not None:
            prev = curr
            curr = curr.next
            tail = curr
        prev.next = head
        tail.next = head.next
        head.next = None
        head = tail
    elif n % 2 == 0 and (k == n // 2 or k == (n // 2) + 1):
        k = n // 2
        # if the element are the middle element next to each other
        prev = head
        first = head.next
        second = first.next
        k -= 1
        while k > 0:
            if k == 1:
                break
            prev = first
            first = second
            second = second.next
            k -= 1
        prev.next = second
        first.next = second.next
        second.next = first

    else:
        first = None
        prev_first = None

        last = None
        prev_last = None

        curr = head

        first_counter = k
        last_counter = n - k

        while first_counter != 0:
            first_counter -= 1

            if first_counter == 1:
                prev_first = curr
                first = curr.next
                curr = curr.next
                break
            curr = curr.next
        curr = head
        while last_counter != 0:
            if last_counter == 1:
                prev_last = curr
                last = curr.next
                break
            curr = curr.next
            last_counter -= 1
        prev_first.next, last.next, first.next, prev_last.next = last, first.next, last.next, first
    # curr = head
    # while curr is not None:
    #     print(curr.data, end=" ")
    #     curr = curr.next
    # print()
    return head


class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

    def __repr__(self):
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


# returns the nth node from end.
def getNthfromEnd(head, n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    while n:
        if n and curr_node == None:
            return None
        curr_node = curr_node.next
        n -= 1

    while curr_node:
        curr_node = curr_node.next
        nth_node = nth_node.next

    return nth_node


# returns the nth node from beg.
def getNthfromBeg(head, n):
    curr_node = head
    for i in range(n - 1):
        if curr_node is None:
            return None
        else:
            curr_node = curr_node.next

    return curr_node


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, kth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        # intial nodes at respective positions.
        check = [
            getNthfromBeg(a.head, kth_node),
            getNthfromEnd(a.head, kth_node)
        ]

        new_head = swapkthnode(a.head, n, kth_node)

        new_check = [
            getNthfromEnd(new_head, kth_node),
            getNthfromBeg(new_head, kth_node)
        ]
        if (check == new_check):
            print(1)
        else:
            print(0)
# } Driver Code Ends