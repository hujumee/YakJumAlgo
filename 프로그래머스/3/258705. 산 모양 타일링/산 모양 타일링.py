def solution(n, tops):
    DIV = 10007
    
    dp = [[0, 0] for _ in range(n) ]
    for i in range(n):
        if i == 0:
            if tops[i]:
                dp[i] = [1, 3]
            else:
                dp[i] = [1, 2]
        else:
            a, b = 0, 0
            if tops[i]:
                a = (dp[i-1][0] + dp[i-1][1]) % DIV
                b = (dp[i-1][0]*2 + dp[i-1][1]*3) % DIV
            else:
                a = (dp[i-1][0] + dp[i-1][1]) % DIV
                b = (dp[i-1][0] + dp[i-1][1]*2) % DIV
            dp[i] = [a, b]
            
    answer = (dp[-1][0] + dp[-1][1]) % DIV
    return answer