N, M = map(int, input().split())
d = dict()

for i in range(N):
    d[input()] = i+1

keys = list(d.keys())

for _ in range(M):
    elem = input()
    if str.isdigit(elem):
        print(keys[int(elem)-1])
    else:
        print(d[elem])

