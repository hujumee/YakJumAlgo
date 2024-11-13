import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

def bfs():
    global nums, ops
    big, small = float('-inf'), float('inf') # 최대값, 최소값
    q = deque([(nums[0], 0, ops)]) 
    while q:
        tmp, index, tmp_ops = q.popleft()
        if index == N-1:
            big = max(big, tmp)
            small = min(small, tmp)
        else:
            for i in range(4):
                next_ops = tmp_ops.copy()
                if tmp_ops[i] > 0:
                    if i == 0:
                        next_tmp = tmp + nums[index+1]
                    elif i == 1:
                        next_tmp = tmp - nums[index+1]
                    elif i == 2:
                        next_tmp = tmp * nums[index+1]
                    elif i == 3:
                        next_tmp = int(tmp / nums[index+1])
                    next_ops[i] -= 1
                    q.append((next_tmp, index+1, next_ops))
    return [big, small]

results = bfs()
print(results[0])
print(results[-1])