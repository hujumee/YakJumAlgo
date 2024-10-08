import sys
input = sys.stdin.readline
import heapq

N = int(input())
lecture = [0] * N

for i in range(N):
    lecture[i]= tuple(map(int, input().split()))
lecture.sort()

room = []
heapq.heappush(room, lecture[0][1])
for i in range(1, N):
    if room[0] <= lecture[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, lecture[i][1])

print(len(room))