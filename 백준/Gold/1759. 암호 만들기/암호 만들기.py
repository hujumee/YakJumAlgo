import sys

N, M = map(int, sys.stdin.readline().split())
char = sys.stdin.readline().split()
char.sort()
vowels = ['a','e','i','o','u']

def dfs(n, prev, temp): # depth, temp[n-2]의 index, 문자열
    if n == N:
        if check(temp):
            print(*temp, sep='')
        return
    
    for i in range(M):
        if visited[i] == 0 and i >= prev:
            visited[i] = 1
            dfs(n+1, i, temp+[char[i]])
            visited[i] = 0

def check(temp):
    c_cnt, v_cnt = 0, 0
    for elem in temp:
        if elem in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
    if v_cnt > 0 and c_cnt > 1:
        return True
    else:
        return False

visited = [0] * M
dfs(0, 0, [])