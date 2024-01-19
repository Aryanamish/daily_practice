#include <bits/stdc++.h>
#define MOD 1000000007;
using namespace std;

int dp[1000001];
int main()

{
    int target;
    cin >> target;

    for (int i = 0; i < target + 1; i++)
    {
        dp[i] = 0;
    }

    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= target; i++)
    {
        for (int j = 1; j < 7; j++)
        {
            if (i - j < 0)
            {
                continue;
            }
            dp[i] = (dp[i] + dp[i - j]) % MOD;
        }
    }
    cout << dp[target];
    return 0;
}