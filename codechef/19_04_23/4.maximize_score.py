# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = abs(arr[0] - arr[1])
    for i in range(1, n-1):
        bob_c_1 = abs(arr[i] - arr[i+1])
        bob_c_2 = abs(arr[i] - arr[i-1])
        ans = min(ans, max(bob_c_1, bob_c_2))
    print(ans)