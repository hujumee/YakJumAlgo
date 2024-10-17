import sys
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())
coins = [0] * N
for i in range(N):
    coins[i] = int(input())
coins.sort()

dp = [INF] * (K+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])