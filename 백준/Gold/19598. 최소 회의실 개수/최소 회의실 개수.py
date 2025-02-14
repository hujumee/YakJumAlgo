# 19598 최소 회의실 개수
import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
arr = [() for _ in range(N)]
for i in range(N):
    arr[i] = tuple(map(int, input().split()))
arr.sort()

mroom = PriorityQueue()
mroom.put(arr[0][1])
for i in range(1, N):
    start, finish = arr[i]
    if start >= mroom.queue[0]:
        mroom.get()
    mroom.put(finish)

print(mroom.qsize())