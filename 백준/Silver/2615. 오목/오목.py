import sys
input = sys.stdin.readline

graph = [[] for _ in range(19)]

for i in range(19):
    temp = input().split()
    for j in range(19):
        elem = int(temp[j])
        graph[i].append(elem)


def check(r, c):
    if c < 15: # 가로 체크
        for i in range(-1, 6):
            if 0 < i < 5:
                if graph[r][c] != graph[r][c+i]:
                    break
            elif i == 0:
                continue
            else:
                if not -1 < c+i < 19:
                    pass
                elif graph[r][c] == graph[r][c+i]:
                    break
            if i == 5:
                return True
    if r < 15: # 세로 체크
        for i in range(-1, 6):
            if 0 < i < 5:
                if graph[r][c] != graph[r+i][c]:
                    break
            elif i == 0:
                continue
            else:
                if not -1 < r+i < 19:
                    pass
                elif graph[r][c] == graph[r+i][c]:
                    break
            if i == 5:
                return True
    if r < 15 and c < 15: # 오른쪽 아래 대각선 체크
        for i in range(-1, 6):
            if 0 < i < 5:
                if graph[r][c] != graph[r+i][c+i]:
                    break
            elif i == 0:
                continue
            else:
                if not ((-1 < r+i < 19) and (-1 < c+i < 19)):
                    pass
                elif graph[r][c] == graph[r+i][c+i]:
                    break
            if i == 5:
                return True
    if r > 3 and c < 15: # 오른쪽 위 대각선 체크
        for i in range(-1, 6):
            if 0 < i < 5:
                if graph[r][c] != graph[r-i][c+i]:
                    break
            elif i == 0:
                continue
            else:
                if not ((-1 < r-i < 19) and (-1 < c+i < 19)):
                    pass
                elif graph[r][c] == graph[r-i][c+i]:
                    break
            if i == 5:
                return True
    return False
            
res = False
for i in range(19):
    for j in range(19):
        if graph[i][j]:
            if check(i, j): # True 리턴값을 받은 경우
                res = True
                print(graph[i][j])
                print(i+1, j+1)
                exit(0)
if not res:
    print(0)
