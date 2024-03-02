import parent
from binary_tree.binary_tree import BinaryTree
from linked_list.queue import Q
import random
from timer import performance

class BFS(BinaryTree):
    @performance(True)
    def breadth_first_search(self):
        q = Q()
        bfs_list = list()
        if self.root is not None:
            q.put(self.root)

        while q.qsize() != 0:
            item = q.get()
            bfs_list.append(item.value)
            if item.left is not None:
                q.put(item.left)
            if item.right  is not None:
                q.put(item.right)
        return bfs_list

bt  = BFS()
l = []
for i in range(0,200): 
    value = int(random.randint(0,2000))
    # while value in l:
        # value = int(random.randint(0,2000))
    l.append(value)
    bt.insert(value)



# print(bt)
bfs = bt.breadth_first_search()
matched = True
for i in l:
    if i not in bfs:
        matched = False
        break
print(matched)
print(len(bfs))
print(len(l))
