#include <bits/stdc++.h>
#define int_max MOD + 2;
#define MOD 1000000007;
using namespace std;

class Solution
{
public:
    int coinChange(vector<int> &coins, int target)
    {
        int n = coins.size();
        vector<vector<int>> dp(n, vector<int>(target + 1, 0));

        for (int i = 0; i <= target; i++)
        {
            if (i % coins[0] == 0)
            {
                dp[0][i] = i / coins[0];
            }
            else
            {
                dp[0][i] = 1e9;
            }
        }

        for (int c = 1; c < n; c++)
        {
            for (int t = 0; t <= target; t++)
            {
                int not_take = dp[c - 1][t];
                int take = 1e9;
                if (t - coins[c] >= 0)
                {
                    take = dp[c][t - coins[c]] + 1;
                }
                dp[c][t] = min(take, not_take);
            }
        }

        return dp[n - 1][target] >= 1e9 ? -1 : dp[n - 1][target];
    }
};

int main()
{
    Solution s;
    int n, target;
    cin >> n >> target;
    vector<int> coins(n);
    for (int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }

    int ans = s.coinChange(coins, target);
    if (ans == -1)
    {
        cout << "-1" << endl;
    }
    else
    {
        cout << ans << endl;
    }

    return 0;
}
