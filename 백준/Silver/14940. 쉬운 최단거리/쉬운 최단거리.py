from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
answer = [[-1 for _ in range(M)]for _ in range(N)]
start = (-1, -1)

for i in range(N):
    temp = input().split()
    for j in range(M):
        elem = int(temp[j])
        graph[i].append(elem)
        if elem == 2:
            start = (i, j)

def BFS(x0, y0):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(x0, y0, 0)]) # x, y, count
    x1, y1 = N, M
    while q:
        x, y, cnt = q.popleft()
        answer[x][y] = cnt
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if -1 < nx < N and -1 < ny < M:
                if (graph[nx][ny] != 0) and (answer[nx][ny] == -1):
                    answer[nx][ny] = cnt+1
                    q.append((nx, ny, cnt+1))
    return

BFS(start[0], start[1])

for i in range(N):
    string = ''
    for j in range(M):
        if graph[i][j] == 0:
            answer[i][j] = 0
        string += str(answer[i][j]) + ' '
    print(string)