import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

empty_cnt = 0
room = [[] for _ in range(N)]
for i in range(N):
    room[i] = list(map(int, input().split()))
    for j in range(M):
        if room[i][j] == 0:
            empty_cnt += 1

def solution(r, c, d):
    move_r = [-1, 0, 1, 0]
    move_c = [0, 1, 0, -1]
    clean_cnt = 0 # 청소한 칸의 개수

    move_possibility = 1
    while move_possibility:
        # 위치하고 있는 좌표가 청소되지 않은 경우
        if room[r][c] == 0:
            room[r][c] = 2 # 2는 벽이 아니고, 청소되었음을 나타냄
            clean_cnt += 1
        
        # 주변 4칸 중 청소되지 않은 빈 칸이 있는지 반시계 방향으로 돌면서 확인
        empty_case = 0 # 빈 칸이 있는지의 여부
        for i in range(1, 5):
            d = (d-1)%4
            tmp_r = r + move_r[d]
            tmp_c = c + move_c[d]
            # 빈 칸이 있는 경우 해당 칸으로 전진
            if room[tmp_r][tmp_c] == 0:
                r, c = tmp_r, tmp_c
                empty_case = 1
                break
        # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if empty_case == 0:
            tmp_d = (d+2)%4 # 후진을 위한 임시 방향
            tmp_r = r + move_r[tmp_d]
            tmp_c = c + move_c[tmp_d]
            if room[tmp_r][tmp_c] != 1:
                # 벽이 아닌 경우 후진
                r, c = tmp_r, tmp_c
            else:
                # 벽이면 작동을 멈춤
                move_possibility = 0
        
        # 모든 빈 칸을 청소했을 경우, 루프 빠져나옴
        if clean_cnt == empty_cnt:
            break
        
    return clean_cnt

print(solution(r, c, d)) 