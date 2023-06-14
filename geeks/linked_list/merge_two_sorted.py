#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''


#Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    head = head1

    prev1 = head1

    curr1 = head1.next
    curr2 = head2

    while curr1 is not None and curr2 is not None:
        if curr1.data > curr2.data:
            temp = curr2.next
            curr2.next = curr1
            prev1.next = curr2
            prev1 = curr2
            curr2 = temp
        else:
            prev1 = curr1
            curr1 = curr1.next

    if curr2 is not None:
        prev1.next = curr2

    return head


'''
5 2 10 15 40
3 20
'''


#{
# Driver Code Starts
#Initial Template for Python 3
# Node Class
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


# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())

        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.

        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))

        for x in nodes_a:
            a.append(x)

        for x in nodes_b:
            b.append(x)

        printList(sortedMerge(a.head, b.head))

# } Driver Code Ends