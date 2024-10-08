T = int(input())

def dp(n):
    arr = [0] * 11
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    if n > 3:
        for i in range(4, n+1):
            arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
    return arr[n]

for _ in range(T):
    N = int(input())
    print(dp(N))
