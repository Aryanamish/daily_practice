for i in range(int(input())):
    n = int(input())
    s = [int(i) for i in input().strip()]
    count1 = 0
    count2 = 1
    
    x1 = [0]
    x2 = [1]
    
    for i in range(1, len(s)):
        x1.append(x1[-1] ^ s[i-1])
        if x1[-1] == 1:
            count1 += 1
        x2.append(x2[-1] ^ s[i-1])
        if x2[-1] == 1:
            count2 += 1
    
    print(max(count1, count2))