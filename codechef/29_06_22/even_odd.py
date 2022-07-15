# cook your dish here
for _ in range(int(input())):
    n = 2*int(input())
    arr = list(map(int, input().split()))
    
    no_of_even = 0
    no_of_odd = 0
    non_multiple_of_four = 0
    for i in arr:
        if i%2 == 0:
            no_of_even += 1
            if i%4 != 0:
                non_multiple_of_four += 1
        else:
            no_of_odd += 1
            
    if no_of_even < no_of_odd:
    
        print(int(abs(no_of_even - (len(arr)//2))))
    elif no_of_even == no_of_odd:
        print(0)
    else:
        if no_of_even - non_multiple_of_four <= no_of_odd + non_multiple_of_four:
            print(int(abs(no_of_even - (len(arr)//2))))
        else:
            even_to_odd = int(abs(no_of_even - (len(arr)//2)))
            no_of_even -= even_to_odd
            no_of_odd += even_to_odd

            ans = int(abs(no_of_even - (len(arr)//2))) * 2 + even_to_odd
            
            
            
            
        
        
        