#include <bits/stdc++.h>
using namespace std;
long long dp[1000001];
int main()
{
	int T;
	cin >> T;

	while (T--)
	{
		long long n;
		cin >> n;

		dp[0] = 1;
		dp[1] = 1;
		dp[2] = 2;
		for (int i = 3; i <= n; i++)
		{
			dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
		}

		cout << dp[n] % 1000000009 << endl;
	}



	return 0;

}