N = int(input())
INT = 1000000000

dp = [[1 for _ in range(10)] for _ in range(N)]
dp[0][0] = 0

for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] 
        elif j == 9:
            dp[i][j] = dp[i-1][8] 
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


res = 0
for i in range(10):
    res += dp[N-1][i]
res %= INT
print(res)