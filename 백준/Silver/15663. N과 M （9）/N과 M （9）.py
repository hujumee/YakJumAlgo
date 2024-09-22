import sys

N, M = map(int, sys.stdin.readline().split())

num = [int(elem) for elem in sys.stdin.readline().split()]
num.sort()
visited = [0]*N
answer = []

def dfs(n, t_list):
    if n == M:
        answer.append(t_list)
        return
    
    prev = 0
    for i in range(N):
        if visited[i] == 0 and prev != num[i]:
            prev = num[i]
            visited[i] = 1
            dfs(n+1, t_list+[num[i]])
            visited[i] = 0

dfs(0, [])
for elem in answer:
    print(*elem)