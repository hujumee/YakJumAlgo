import sys
input = sys.stdin.readline

N, D = map(int, input().split())
roads = [0] * N
for i in range(N):
    roads[i] = tuple(map(int, input().split()))
roads.sort()

def calculate_min(roads):
    distance = [n for n in range(10001)]
    for road in roads:
        start, end, dist = road
        if start < D and end <= D:
            distance[end] = min(distance[end], distance[start]+dist)
            for n in range(1, D+1-end):
                distance[end+n] = min(distance[end+n], distance[end]+n)
    return distance[D]

print(calculate_min(roads))