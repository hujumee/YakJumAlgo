import sys
input = sys.stdin.readline

N = int(input())
wine = [0] * N
for i in range(N):
    wine[i] = int(input())

visited = [0] * N
dp = [0] * N

dp[0] = wine[0]
if N > 1:
    dp[1] = wine[0]+wine[1]
if N > 2:
    dp[2] = max(wine[2]+wine[1], wine[2]+wine[0], dp[1])
if N > 3:
    for i in range(3, N):
        dp[i] = max(dp[i-1], wine[i]+wine[i-1]+dp[i-3], wine[i]+dp[i-2])

print(dp[N-1])