# cook your dish here
int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	   int n,f=0;
	   string a;
	   cin>>n>>a;
	   map<char,int>a1,b;
	   for(int i=0;i<n;i++)
	   {
	       if(i%2==0)b[a[i]]++;
	       else a1[a[i]]++;
	   }
	   for (auto& itr:a1)
	   {
	       if(b[itr.first]!=itr.second)
	       {
	           f=1;
	           break;
	       }
	   }
	   if (f)
	   cout<<"no"<<endl;
	   else
	   cout<<"yes"<<endl;
	}
	return 0;
}

def inc(d, key):
    if d.get(key) is None:
        d[key] = 1
    else:
        d[key] = d[key] + 1

def solve(n, s):
    f = False
    a1, b = {}, {}
    for i in range(0, n):
        if i%2 ==0:
            inc(b, s[i])
        else:
            inc(a1, s[i])
    
    for i in a1:
        if b[i] != a1[i]:
            f = True
            break
    if f is True:
        return 'NO'
    else:
        return "YES"

for _ in range(int(input())):
    print(solve(int(input()), input()))