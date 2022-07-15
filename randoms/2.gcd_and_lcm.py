def min_max(a,b):
    return min(a,b), max(a,b)

def compute_lcm(a,b, hcf=None):
    return abs(a*b)/hcf

def compute_hcf(x,y):
    while(y):
        c+=1
        x, y = y, x % y
    return x
    
def calc(a,b):
    hcf = compute_hcf(a,b)
    lcm = compute_lcm(a,b, hcf)
    return int(a*a + b*b + hcf*hcf + lcm*lcm)

def solve(n):
    count = 0
    for i in range(1,n):
        if (4*i*i) > n:
            break
        for j in range(i, n):
            i_j = calc(i,j)
            if i_j > n:
                break
            elif i_j == n:
                if i != j:
                    count += 2
                else:
                    count += 1
    print(count) 
    

# for _ in range(int(input())):
    # solve(int(input()))
print(compute_hcf(10**10, 1578347894))
    
    
    