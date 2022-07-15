for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    if k == 1:
        print('YES')
        [print(i) for i in range(1, n+1)]
        continue
    odd_no = n*k //2
    odd_no = odd_no  if (n*k)%2 == 0 else odd_no + 1
    even_no = (n*k) - odd_no
    
    if odd_no%k == 0 and even_no%k == 0:
        print("YES")
        count = 1
        for i in range(1, n*k+1, 2):
            if count%k == 0:
                print(i)
            else:
                print(i, end=" ")
            count += 1
        count = 1
        for i in range(2, n*k+1, 2):
            if count%k == 0:
                print(i)
            else:
                print(i, end=" ")
            count += 1

    else:
        print("NO")
