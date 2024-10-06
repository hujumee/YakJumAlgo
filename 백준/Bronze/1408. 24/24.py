import sys
input = sys.stdin.readline

now = list(map(int, input().split(':')))
start = list(map(int, input().split(':')))

remain = [0] * 3

if now[2] <= start[2]:
    remain[2] = start[2] - now[2]
else:
    remain[2] = start[2]+60 - now[2]
    start[1] -= 1

if now[1] <= start[1]:
    remain[1] = start[1] - now[1]
else:
    remain[1] = start[1]+60 - now[1]
    start[0] -= 1

if now[0] <= start[0]:
    remain[0] = start[0] - now[0]
else:
    remain[0] = start[0]+24 - now[0]

answer = ''
for elem in remain:
    if elem >= 10:
        answer += str(elem)+':'
    else:
        answer += '0'+str(elem)+':'
print(answer[:8])