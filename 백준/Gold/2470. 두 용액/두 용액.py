import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

def pick(arr):
    n = len(arr)
    i, j = 0, n-1 # 투 포인터
    s1, s2 = i, j # 정답이 되는 용액
    val = arr[i] + arr[j]
    while i < j:
        if arr[i]+arr[j] == 0:
            s1, s2 = i, j
            break
        elif abs(arr[i]+arr[j]) < abs(val):
            s1, s2 = i, j
            val = arr[i]+arr[j]
        elif arr[i]+arr[j] > 0:
            j -= 1
        elif arr[i]+arr[j] < 0:
            i += 1
    return [arr[s1], arr[s2]]

print(*pick(solutions))
