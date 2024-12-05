X, Y = input(), input()
x, y = len(X), len(Y)


def solution(x, y):
    if x == 0 or y == 0:
        return 0
    
    dp = [[0 for _ in range(x)] for _ in range(y+1)]

    for i in range(y):
        for j in range(x):
            if X[j] == Y[i]:
                if j == 0:
                    dp[i+1][j] = max(dp[i][j], 1)
                else:
                    dp[i+1][j] = max(dp[i+1][j-1], dp[i][j-1]+1)
            else:
                if j == 0:
                    dp[i+1][j] = max(dp[i][j], dp[i+1][j])
                else:
                    dp[i+1][j] = max(dp[i+1][j-1], dp[i][j])

    return dp[y][x-1]

print(solution(x, y))

