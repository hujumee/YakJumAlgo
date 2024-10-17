import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [0] * N
for i in range(N):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    graph[i] = (x,y)
graph.sort()

lines = deque([graph[0]])
for i in range(1, N):
    x, y = graph[i]
    x0, y0 = lines[-1]
    if x > y0:
        lines.append((x,y))
    else:
        if y > y0:
            lines.pop()
            lines.append((x0, y))

res = 0
for x, y in lines:
    res += y-x
print(res)