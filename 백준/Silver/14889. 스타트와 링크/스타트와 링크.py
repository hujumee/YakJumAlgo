import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
score = [[] for _ in range(N)]
for i in range(N):
    score[i] = list(map(int, input().split()))

def dfs(i, j): #몇명째 방문인지, 마지막으로 추가한 사람의 인덱스
    global result, score, N, visited

    if i == N//2:
        S_score, L_score = 0, 0

        for k in range(N):
            for l in range(N):
                if k == l:
                    continue
                if visited[k] and visited[l]:
                    S_score += score[k][l]
                elif not visited[k] and not visited[l]:
                    L_score += score[k][l]
        
        result = min(result, abs(S_score - L_score))
        return 
    
    elif j == N:
        return
    
    for k in range(j, N):
        if not visited[k]:
            visited[k] = 1
            dfs(i+1, k+1)
            visited[k] = 0


visited = [0] * N
result = INF
dfs(0,0)
print(result)