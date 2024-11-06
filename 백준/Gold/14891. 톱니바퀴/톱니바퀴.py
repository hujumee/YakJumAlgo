import sys
input = sys.stdin.readline

A, B, C, D = input(), input(), input(), input()
a, b, c, d = 0, 0, 0, 0 # 12시 방향을 가리키는 인덱스

N = int(input())
rotate = [0] * N
for i in range(N):
    rotate[i] = tuple(map(int, input().split()))


def rotateA(dir_a):
    a3, b9, b3, c9, c3, d9 = (a+2)%8, (b-2)%8, (b+2)%8, (c-2)%8, (c+2)%8, (d-2)%8 # 각 톱니의 3시, 9시 방향 인덱스
    dir_b, dir_c, dir_d = 0, 0, 0 
    if A[a3] != B[b9]:
        dir_b = -dir_a
        if B[b3] != C[c9]:
            dir_c = -dir_b
            if C[c3] != D[d9]:
                dir_d = -dir_c
    return (dir_a, dir_b, dir_c, dir_d)

def rotateB(dir_b):
    a3, b9, b3, c9, c3, d9 = (a+2)%8, (b-2)%8, (b+2)%8, (c-2)%8, (c+2)%8, (d-2)%8 # 각 톱니의 3시, 9시 방향 인덱스
    dir_a, dir_c, dir_d = 0, 0, 0
    if A[a3] != B[b9]:
        dir_a = -dir_b
    if B[b3] != C[c9]:
        dir_c = -dir_b
        if C[c3] != D[d9]:
            dir_d = -dir_c
    return (dir_a, dir_b, dir_c, dir_d)

def rotateC(dir_c):
    a3, b9, b3, c9, c3, d9 = (a+2)%8, (b-2)%8, (b+2)%8, (c-2)%8, (c+2)%8, (d-2)%8 # 각 톱니의 3시, 9시 방향 인덱스
    dir_a, dir_b, dir_d = 0, 0, 0
    if C[c9] != B[b3]:
        dir_b = -dir_c
        if B[b9] != A[a3]:
            dir_a = -dir_b
    if C[c3] != D[d9]:
        dir_d = -dir_c
    return (dir_a, dir_b, dir_c, dir_d)

def rotateD(dir_d):
    a3, b9, b3, c9, c3, d9 = (a+2)%8, (b-2)%8, (b+2)%8, (c-2)%8, (c+2)%8, (d-2)%8 # 각 톱니의 3시, 9시 방향 인덱스
    dir_a, dir_b, dir_c = 0, 0, 0
    if D[d9] != C[c3]:
        dir_c = -dir_d
        if C[c9] != B[b3]:
            dir_b = -dir_c
            if B[b9] != A[a3]:
                dir_a = -dir_b
    return (dir_a, dir_b, dir_c, dir_d)

def score():
    res = 0
    if A[a] == '1':
        res += 1
    if B[b] == '1':
        res += 2
    if C[c] == '1':
        res += 4
    if D[d] == '1':
        res += 8
    return res


def solution():
    global a, b, c, d
    for arg in rotate:
        num, dir = arg
        if num == 1:
            dir_a, dir_b, dir_c, dir_d = rotateA(dir)
        elif num == 2:
            dir_a, dir_b, dir_c, dir_d = rotateB(dir)
        elif num == 3:
            dir_a, dir_b, dir_c, dir_d = rotateC(dir)
        elif num == 4:
            dir_a, dir_b, dir_c, dir_d = rotateD(dir)
        a = (a - dir_a)%8
        b = (b - dir_b)%8
        c = (c - dir_c)%8
        d = (d - dir_d)%8
    return score()

print(solution())


