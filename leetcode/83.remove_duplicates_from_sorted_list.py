class ListNode:
    def __init__(self, value=0):
        self.val = value
        self.next = None
    def __str__(self):
        node = self
        values = []
        while node:
            values.append(str(node.val))
            node = node.next
        
        return f"{' -- > '.join(values)}"

    def __repr__(self):
        return self.__str__()

class SingleLinkedList:
    Node = ListNode
    def __init__(self, value):
        self.head_node = ListNode(value)
        self.last_node = self.head_node
        self.length = 1

    def __get_nth_nodes__(self, index):
        if index < self.length:
            i = 0
            next_node = self.head_node
            while(i < index):
                next_node = next_node.next
                i += 1
            return next_node
        elif index >= self.length:
            raise IndexError("LinkedList index out of range")

    def append(self, value):
        self.last_node.next = self.Node(value)
        self.last_node = self.last_node.next
        self.length += 1
        return self.last_node
    def prepend(self, value):
        new_head = self.Node(value)
        new_head.next = self.head_node
        self.head_node = new_head
        self.length += 1

    def reverse(self):
        if self.length == 1:
            return None
        first = self.head_node
        second = first.next
        while second is not None:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head_node, self.last_node = self.last_node, self.head_node



    def insert(self, index, value):
        if index == self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            node = self.__get_nth_nodes__(index-1)
            next_node = node.next
            node.next = ListNode(value)
            node.next.next = next_node
            self.length += 1

    def replace(self, index, value):
        node = self.__get_nth_nodes__(index)
        node.val = value

    def delete(self, index):
        if index == 0:
            deleted_node = self.head_node
            self.head_node = deleted_node.next
            self.length -= 1
        elif index >= self.length:
            raise IndexError("Listindex out of range")
        else:
            node = self.__get_nth_nodes__(index-1)
            deleted_node = node.next
            node.next = node.next.next
            self.length -= 1
        return deleted_node

    def get(self, index):
        return self.__get_nth_nodes__(index)

    def __getitem__(self, index):
        return self.__get_nth_nodes__(index).val
    
    def __setitem__(self, index, value):
        self.replace(index, value)

    def __get_all_value__(self):
        node = self.head_node
        values = [node.val]
        for _ in range(0, self.length-1):
            node = node.next
            values.append(node.val)
        return values


    def __str__(self):
        value = map(repr, self.__get_all_value__())
        return f"[{' --> '.join(value)}]"
    
    def __repr__(self):
        return self.__str__()
        
class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        new_head = ListNode(None)
        curr_node = new_head
        previous_node = new_head
        
        while head:
            if head.val != previous_node.val:
                curr_node.val = head.val
                previous_node = curr_node
                curr_node.next = ListNode(None)
                curr_node = curr_node.next
            head = head.next
        previous_node.next = None
        return new_head
        


if __name__ == '__main__':
    ls = SingleLinkedList(0)
    ls.append(0)
    ls.append(2)
    ls.append(2)
    ls.append(2)
    s = Solution()
    print(s.deleteDuplicates(ls.head_node))