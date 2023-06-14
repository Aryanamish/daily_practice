#User function Template for python3
class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:

    def __str__(self):
        l = []
        curr = self.head
        while curr is not None:
            l.append(curr.data)
            curr = curr.next
        l.reverse()
        return str(l)

    def __repr__(self):
        return self.__str__()

    def __init__(self):
        self.length = 0
        self.head = None

    def append(self, value):
        node = Node(value, self.head)
        self.head = node
        self.length += 1

    @property
    def isEmpty(self):
        return True if self.length == 0 else False

    def peek(self):
        return self.head.data if self.head is not None else None

    def pop(self):
        if self.head is not None:
            val = self.head.data
            self.head = self.head.next
            self.length -= 1
            return val
        return None


class Solution:

    oper = {
        "(": [1, 'ltr'],
        ")": [1, 'ltr'],
        "+": [2, "ltr"],
        "-": [2, "ltr"],
        "*": [3, "ltr"],
        "/": [3, "ltr"],
        "^": [4, "rtl"],
    }

    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        string = ''
        stack = Stack()
        for i in exp:
            prio = self.oper.get(i)
            if prio is None:
                string += i
            else:
                if stack.isEmpty:
                    stack.append(i)
                else:
                    if i == "(":
                        stack.append(i)
                    elif i == ")":
                        while stack.isEmpty is False:
                            t = stack.pop()
                            if t == "(":
                                break
                            string += t
                    else:
                        top_prio = self.oper.get(stack.peek())
                        if prio[0] > top_prio[0]:
                            stack.append(i)
                        else:
                            while stack.isEmpty is False:
                                top = stack.peek()
                                top_prio = self.oper.get(top)
                                if top_prio[0] < prio[0] or top == "(":
                                    break
                                string += stack.pop()

                            stack.append(i)

        while stack.isEmpty is False:
            top = stack.pop()
            if top == "(" or top == ")":
                continue
            string += top
        return string


if __name__ == '__main__':
    # test_cases = int(input())
    for cases in range(1):
        # exp = str(input())
        ob = Solution()
        print(ob.InfixtoPostfix("a+b*(c^d-e)^(f+g*h)-i"))
# } Driver Code Ends