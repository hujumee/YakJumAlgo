import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int,input().split())

graph = [[[] for _ in range(N)] for _ in range(H)]
tomatoes_cnt = 0 # 토마토 개수
ripen = [] # 익은 토마토의 위치 저장

for i in range(H):
    for j in range(N):
        temp = input().split()
        for k in range(M):
            elem = int(temp[k])
            if elem == 1:
                tomatoes_cnt += 1
                ripen.append((i,j,k))
            elif elem == 0:
                tomatoes_cnt += 1
            graph[i][j].append(elem)


def BFS(ripen):
    dc = [0, 0, 0, 0, 1, -1]
    dr = [0, 0, 1, -1, 0, 0]
    dh = [1, -1, 0, 0, 0, 0]

    q = deque([])
    for tomato in ripen:
        q.append((*tomato, 0)) # 높이, 행, 열, 걸린 날
    res = 0 # 리턴할 값: 걸린 일 수
    while q:
        h, r, c, cnt = q.popleft()
        for i in range(6):
            nh, nr, nc = h+dh[i], r+dr[i], c+dc[i]
            if (-1 < nh < H) and (-1 < nr < N) and (-1 < nc < M): # 유효 범위 내인지 확인
                if graph[nh][nr][nc] == 0: # 안익은 토마토인지 확인
                    graph[nh][nr][nc] = 1 # 익은 토마토로 바꿔주기
                    ripen.append((nh, nr, nc)) # 익은 토마토 리스트에 추가
                    q.append((nh, nr, nc, cnt+1))
        if cnt > res:
            res = cnt
    return res



if tomatoes_cnt == len(ripen):
    print(0)
else:
    cnt = BFS(ripen)
    if tomatoes_cnt == len(ripen):
        print(cnt)
    else:
        print(-1)