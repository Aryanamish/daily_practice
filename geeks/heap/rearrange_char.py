#User function Template for python3
import heapq


#Function to rearrange the characters in a string such that
#no two adjacent characters are same.
def rearrangeString(s):

    arr = [0] * 26
    for i in s:
        arr[ord(i) % 97] += 1
    char = []
    for i in range(0, 26):
        if arr[i] > 0:
            char.append([arr[i], chr(i + 97)])
    heapq._heapify_max(char)
    new_str = ''
    stack = []
    while len(char) > 0:
        if len(stack) > 0 and stack[-1][1] != new_str[-1]:
            c = stack.pop()
        else:
            c = heapq._heappop_max(char)
        new_str += c[1]
        c[0] -= 1
        if c[0] <= 0:
            continue
        if c[0] > char[0][0]:
            stack.append(c)
        elif c[0] > 0:
            char.append(c)
            heapq._heapify_max(char)

    print(new_str)
    return new_str


def checker(s, res):
    freq = [0] * 26
    if (len(s) != len(res)):
        return 0
    n = len(s)
    for i in range(n):
        freq[ord(s[i]) - 97] -= 1
        if (ord(res[i]) < 97 or ord(res[i]) > 122):
            return 0
        freq[ord(res[i]) - 97] += 1
    for i in freq:
        if i != 0:
            return 0
    for i in range(n - 1):
        if res[i] == res[i + 1]:
            return 0
    return 1


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        res = rearrangeString(s)
        print(checker(s, res))

# } Driver Code Ends