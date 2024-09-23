import sys

N, M = map(int, sys.stdin.readline().split())
house, chicken = [], []
for i in range(N):
    temp = sys.stdin.readline().split()
    for j in range(N):
        if int(temp[j]) == 1:
            house.append((i, j))
        elif int(temp[j]) == 2:
            chicken.append((i, j))

answer = []
visited = [0] * len(chicken)

def dfs(n, prev, temp): # M개의 치킨집을 고르고, 고를때마다 최소의 치킨 거리를 저장하는 함수
    if n == M:
        answer.append(min_dist(temp))
        return
    
    for i in range(len(chicken)):
        if visited[i] != 1 and i >= prev:
            visited[i] = 1
            dfs(n+1, i, temp+[chicken[i]])
            visited[i] = 0


def min_dist(M_chicken): # M개의 치킨집과 도시의 치킨 거리의 최솟값 계산
    dist_list = [[0 for _ in range(M)] for _ in range(len(house))]
    for i in range(len(house)):
        for j in range(len(M_chicken)):
            dist_list[i][j] = abs(house[i][0]-M_chicken[j][0]) + abs(house[i][1]-M_chicken[j][1])
   
    res = 0
    for dist in dist_list:
        res += min(dist)
    return res

answer = []
if M < len(chicken):
    dfs(0, 0, [])
else:
    answer.append(min_dist(chicken))
print(min(answer))