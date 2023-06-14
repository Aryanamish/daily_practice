#User function Template for python3
'''
class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
'''


#Function to return the decoded string.
def get_code(node, string, code):

    if node is None:
        return
    else:
        if node.data != '$':
            code[string] = [node.data, node.freq]
        else:
            get_code(node.left, string + '0', code)
            get_code(node.right, string + '1', code)


def decodeHuffmanData(root, binaryString):
    code = {}
    get_code(root, '', code)
    print(code)


#{
# Driver Code Starts
#Initial Template for Python 3

import heapq

minheap = []
heapq.heapify(minheap)
cnt = 0
codes = {}
freq = {}


class MinHeapNode:

    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data) + f" ({self.freq})"

    def __str__(self) -> str:
        return self.__repr__()


def printCodes(root, strr):
    if root == None:
        return
    if root.data != '$':
        print(str(root.data) + ": " + strr)
    printCodes(root.left, strr + "0")
    printCodes(root.right, strr + "1")


def storeCodes(root, strr):
    if root == None:
        return
    if root.data != '$':
        codes[root.data] = strr
    storeCodes(root.left, strr + "0")
    storeCodes(root.right, strr + "1")


def huffmanCodes(s):
    global cnt
    for v in freq:
        heapq.heappush(minheap,
                       (freq[v], freq[v] + cnt, MinHeapNode(v, freq[v])))
        cnt += 1
    while (len(minheap) != 1):
        left = minheap[0][2]
        heapq.heappop(minheap)
        right = minheap[0][2]
        heapq.heappop(minheap)
        top = MinHeapNode('$', left.freq + right.freq)
        top.left = left
        top.right = right
        heapq.heappush(minheap, (top.freq, top.freq + cnt, top))
        cnt += 1
    storeCodes(minheap[0][2], "")


def calcFreq(strr, n):
    for i in range(n):
        if strr[i] not in freq:
            freq[strr[i]] = 1
        else:
            freq[strr[i]] += 1


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        strr = input()
        encodedString = ""
        decodedString = ""
        calcFreq(strr, len(strr))
        #print(freq)
        huffmanCodes(len(strr))
        #print(codes)
        for i in strr:
            encodedString += codes[i]

        decodedString = decodeHuffmanData(minheap[0][2], encodedString)
        print(decodedString)
        t = t - 1

# } Driver Code Ends