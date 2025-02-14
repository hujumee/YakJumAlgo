from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
position = list(map(int, sys.stdin.readline().split()))
q = deque([0 for i in range(n)])

for i in range(len(position)):
    q[position[i]-1] = i+1 # 뽑아내야 하는 순서대로 해당 인덱스의 원소 변경

answer = 0
cur_i = 1

for i in range(m):
    cnt = 0
    while (q[0] != i+1):
        q.rotate(1)
        cnt += 1
    if (cnt > n/2):
        cnt = n - cnt
    q.popleft()
    n -= 1
    answer += cnt
    if (i < m-1):
        cur_i = position[i+1]%n # 현재 위치 확인

print(answer)