import sys
input = sys.stdin.readline

N = int(input())
signs = input().split()
max_n, min_n = 0, float("inf")
check = [0] * 10

def dfs(i, k, tmp):
    global max_n, min_n
    if i == N+1:
        tmp_int = 0
        for elem in tmp:
            tmp_int = tmp_int*10 + int(elem)
        min_n = min(tmp_int, min_n)
        max_n = max(tmp_int, max_n)
        return
    

    if i == 0:
        for j in range(0, 10):
            tmp.append(j)
            check[j] = 1
            dfs(i+1, j, tmp)
            tmp.pop()
            check[j] = 0

    elif signs[i-1] == '<':
        for j in range(k+1, 10):
            if not check[j]:
                tmp.append(j)
                check[j] = 1
                dfs(i+1, j, tmp)
                tmp.pop()
                check[j] = 0

    elif signs[i-1] == '>':
        for j in range(0, k):
            if not check[j]:
                tmp.append(j)
                check[j] = 1
                dfs(i+1, j, tmp)
                tmp.pop()
                check[j] = 0
    return

dfs(0, 0, [])
print(str(max_n))
print(str(min_n).zfill(N+1))