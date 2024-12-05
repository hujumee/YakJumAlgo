import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    graph[i] = tmp

def bfs(r, c, graph): # 시작점의 행번호, 열번호, 움직일 그래프
    q = deque([(0, r, c)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[r][c] = 1
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    answer = (0, 0) # cnt, 처음+끝

    while q:
        cnt, tmp_r, tmp_c = q.popleft()
        # 최장거리, 최대합 갱신
        if cnt > answer[0]:
            tmp_sum = graph[r][c]+graph[tmp_r][tmp_c]
            answer = (cnt, tmp_sum)
        elif cnt == answer[0]:
            tmp_sum = graph[r][c]+graph[tmp_r][tmp_c]
            if tmp_sum > answer[1]:
                answer = (cnt, tmp_sum)

        for i in range(4):
            new_r, new_c = tmp_r+dr[i], tmp_c+dc[i]
            if 0 <= new_r < N and 0 <= new_c < M and graph[new_r][new_c]: # 그래프의 범위 내에 존재하고, 0이 아닌지 검사
                if not visited[new_r][new_c]: # 이미 지나간 곳인지 검사
                    visited[new_r][new_c] = 1
                    q.append((cnt+1, new_r, new_c))
    return answer

def solution(graph):
    passwds = []

    for i in range(N):
        for j in range(M):
            if graph[i][j]: # (j,i)의 값이 0이 아니면
                tmp = bfs(i, j, graph)
                passwds.append(tmp)

    if len(passwds) == 0:
        return 0
    passwds.sort(reverse=True)
    return passwds[0][1]

print(solution(graph))