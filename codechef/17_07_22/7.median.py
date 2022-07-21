#include <iostream> 
#include<bits/stdc++.h> 
using namespace std; 
 
int main() { 
 // your code goes here 
  
  
 int t; 
 cin>>t; 
 while(t--) 
 { 
     int n; 
     cin>>n; 
     vector<long long> y(n); 
      
     vector<long long> x(n); 
      
     for(long long i=0;i<n;i++) 
     { 
         cin>>y[i]; 
     } 
      
     sort(y.begin(),y.end()); 
     for(long long i=0;i<n;i++) 
     { 
         cin>>x[i]; 
     } 
      
     sort(x.begin(),x.end()); 
      
     vector<long long> ans; 
      
      
      
      
      
     for(long long i=n/2;i<n;i++) 
     { 
         ans.push_back(y[i]); 
     } 
    y=ans; 
     ans.clear(); 
     
     for(long long i=n/2;i<n;i++) 
     { 
         ans.push_back(x[i]); 
    } 
     
    x=ans; 
     n=x.size(); 
      
     vector<long long> cty; 
       for(long long i=0;i<n;i++) 
     { 
         cty.push_back(x[i]+y[n-1-i]); 
     } 
      
     sort(cty.begin(),cty.end()); 
      
          
      
      
      
     cout<<cty[0]<<endl; 
      
      
      
      
 } 
 return 0; 
}


def solve(n, x, y):
    x.sort()
    y.sort()

    ans = []

    for i in range(n//2, n):
        ans.append(y[i])
    
    y = ans
    ans = []

    for i in range(n//2, n):
        ans.append(x[i])

    x = ans
    n = len(x)
    cty = []
    for i in range(n):
        cty.append(x[i] + y[n-1-i])

    cty.sort()

    return cty[0]

for _ in range(int(input())):
    solve(
        int(input()),
        list(map(int, input().split())),
        list(map(int, input().split())),
    )
    