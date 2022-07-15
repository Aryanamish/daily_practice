# cook your dish here
def count_bracket(s):
    opn = close = 0
    for i in s:
        if i == '(':
           opn += 1
        else:
            close += 1    
    
    return opn, close
        
def solve(n, s):
    count  = 0
    if n == 0:
        return 0
    if n%2 != 0:
        i = 0
        stack = list()
        while i < n:
            if s[i] =='(':
                stack.append(s[i])
            if s[i] == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    s = s[:i] + s[i+1:]
                    count += 1
            i+=1


                
            
            
    mid = n//2
    first_half_open_bracket , first_half_close_bracket = count_bracket(s[:mid])
    second_half_open_bracket , second_half_close_bracket = count_bracket(s[mid:])
    if first_half_open_bracket != second_half_close_bracket:
        count = abs(first_half_open_bracket - second_half_close_bracket)
    
    return first_half_close_bracket + second_half_open_bracket + count
    

for _ in range(int(input())):
    print(solve(int(input()), input()))