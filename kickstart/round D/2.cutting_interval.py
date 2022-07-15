try:
    from run import read_input
    read = read_input()
    input = read.input
except ImportError:
   pass


class Node:
    def __init__(self, value=None, previous_node=None, next_node=None):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node
        self.ends_with = []
        self.cross_path = 0

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return repr(self.value)


class DoublyLinkedList:
    Node = Node
    def __init__(self, value=None):
        self.head = self.Node(value)
        self.tail = self.head
        self.length = 0

    def reverse(self):
        current_node = self.head
        while current_node is not None:
            temp = current_node.previous_node
            current_node.previous_node  = current_node.next_node
            current_node.next_node = temp
            current_node = current_node.previous_node


        self.tail , self.head = self.head, self.tail
        


    def lookup(self, index):
        if index >= self.length:
            raise IndexError("LinkedList index out of range")
        elif index <= self.length/2:
            i = 0
            current_node = self.head
            while(i < index):
                current_node = current_node.next_node
                i += 1
            return current_node
        elif index > self.length/2:
            i = self.length - 1
            current_node = self.tail
            while(i < index):
                current_node = current_node.previous_node
                i -= 1
            return current_node


    
    def insert_behind(self, node, value):
        # 1 <-> 5
        if node.value == value:
            return
        new_node = self.Node(value, node.previous_node, node)
        node.previous_node.next_node = new_node
        node.previous_node = new_node       
        self.length += 1 
        return new_node
        
    def append(self, value):
        new_node = self.Node(value, self.tail, None)
        self.tail.next_node = new_node
        self.tail = new_node
        self.length += 1
        return new_node
    
    def insert(self, a, b):
        if b-a <= 1:
            return

        
        if self.head.value is None:
            self.head.value = a
            self.head.ends_with.append(b)
            self.tail = self.Node(b, self.head, None)
            self.head.next_node = self.tail
            self.length += 2
        elif a > self.tail.value:
            self.append(a).ends_with.append(b)
            self.append(b)
            return
        else:
            node = self.head
            a_inserted, b_inserted = False, False
            while node is not None:
                if a == node.value:
                    a_inserted = True
                    node.ends_with.append(b)
                if b == node.value:
                    b_inserted = True
                if (a < node.value or node.next_node is None) and a_inserted is False:
                    self.insert_behind(node, a).ends_with.append(b)
                    a_inserted = True
                if (b < node.value or node.next_node is None) and b_inserted is False:
                    self.insert_behind(node, b)
                    b_inserted = True
                
                if a_inserted and b_inserted:
                    break
               
                node = node.next_node



    def __setitem__(self, index, value):
        self.replace(index, value)

    def __getitem__(self, index):
        return self.lookup(index).value

    def __get_all_value__(self):
        node = self.head
        values = [str(node.value) + str(node.ends_with) if len(node.ends_with) > 0 else str(node.value)]
        while(node.next_node is not None):
            node = node.next_node
            values.append(str(node.value) + str(node.ends_with) if len(node.ends_with) > 0 else str(node.value))
        return values

    def __str__(self):
        value = map(repr, self.__get_all_value__())
        return f"[{' <--> '.join(value)}]"
    
    def __repr__(self):
        return self.__str__()

for count in range(int(input(""))):
    N, C = list(map(int, input("").split(' ')))
    intervals = [list(map(int, input("").split(' '))) for _ in range(N)]

    a = DoublyLinkedList()
    a.insert(1,5)
    a.insert(2,4)
    a.insert(3,3)
    a.insert(10,100)
    a.insert(10,12)

    print(a)