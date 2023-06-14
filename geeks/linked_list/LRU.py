#User function Template for python3

# design the class in the most optimal way


class Node:

    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.key) + "->" + str(self.value)

    def __repr__(self):
        return str(self.key) + "->" + str(self.value)


class LinkedList:

    def __repr__(self):
        string = ""
        curr = self.head
        for i in range(0, self.length):
            string += str(curr) + " => "
            curr = curr.next
        return string[:-4] + " (" + str(self.length) + ")"

    def __str__(self):
        return self.__repr__()

    def __init__(self, key, value, cap):
        self.cap = cap
        self.head = Node(key, value)
        self.tail = self.head
        self.length = 1
        self.hash = {key: self.head}

    def remove_tail(self):
        rv = self.tail
        if self.tail.prev is None:
            self.tail = None
            self.head = None
        else:
            tail = self.tail.prev
            tail.next = None
            self.tail = tail
        del self.hash[rv.key]
        rv.prev = None
        rv.next = None
        return rv

    def add_head(self, node):
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.hash[node.key] = node
        return self.head

    def move_node_forward(self, node):
        if node == self.head:
            return
        if node == self.tail:
            tail = self.remove_tail()
            self.add_head(tail)
            # tail = self.tail.prev
            # tail.next = None
            # node.prev = None
            # node.next = self.head
            # self.head.prev = node
            # self.head = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

    def find(self, key):
        if key in self.hash:
            node = self.hash.get(key)
            self.move_node_forward(node)
            return node
        return None

    def insert(self, key, value):

        node = self.find(key)
        if node is None:
            node = Node(key, value, None, self.head)
            self.add_head(node)
            if self.length == self.cap:
                self.remove_tail()
            else:
                self.length += 1
        else:
            node.value = value


class LRUCache:

    def __repr__(self):
        return "LRU: " + self.data.__str__()

    def __str__(self):
        return self.data.__str__()

    #Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.cap = cap
        self.data = None

    @property
    def length(self):
        return self.data.length

    #Function to return value corresponding to the key.
    def get(self, key):
        if self.data is None:
            return -1
        node = self.data.find(key)
        return node.value if node is not None else -1

    #Function for storing key-value pair.
    def set(self, key, value):
        if self.data is None:
            self.data = LinkedList(key, value, self.cap)
        else:
            self.data.insert(key, value)


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  #number of queries
        a = list(map(str,
                     input().strip().split()))  # parent child info in list

        lru = LRUCache(cap)

        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]

            if qtyp == 'SET':
                lru.set(int(a[i + 1]), int(a[i + 2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i + 1])), end=' ')
                i += 2
            q += 1
        print()
# } Driver Code Ends