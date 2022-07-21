#include <bits/stdc++.h>
#define ll long long
# using namespace std;
# void solve(){
#     vector<ll>x;
#     ll z=0;
#     for(ll i=0;i<q;i++)
#     {
#         ll y;
#         cin>>y;
#         if(y==0)
#         z++;
#         else
#         x.push_back(y);
    
    
#     }
#     sort(x.begin(),x.end());
#     for(ll i=0;i<z;i++)
#     x.push_back(0);
    
#     ll o=0,p=1;
#     for(ll i=0;i<q;i++)
#     {
#         int f=1;
#         for(ll k=0;k<x[i];k++)
#     {
#         if(p<q)
#         p++;
#         else{
#             f=0; break;
#         }
#     }
#     o+=f;
#     }
#     cout<<o<<endl;
# }




def solve(n, x):
    zero = []
    i = 0
    while i < len(x):
        if x[i] == 0:
            del x[i]
            zero.append(0)
        else:
            i+=1
    x.sort()
    x += zero
    o=0
    p = 1
    for i in range(n):
        f = 1
        for k in range(x[i]):
            if p<n:
                p += 1
            else:
                f = 0
                break
        o += f
    return o
for _ in range(int(input())):
    print(solve(int(input()), list(map(int, input().split()))))