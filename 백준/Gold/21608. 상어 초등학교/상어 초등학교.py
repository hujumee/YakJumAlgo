import sys
input = sys.stdin.readline

N = int(input())
students = [0] * (N**2)
likes = dict([]) # 좋아하는 학생
for i in range(N**2):
    s0, s1, s2, s3, s4 = map(int, input().split())
    students[i] = s0
    likes[s0] = [s1, s2, s3, s4]


# 만족도의 합을 계산하는 함수
def satisfaction(likes, seats):
    res = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            s = seats[i][j]
            cnt = 0 # 인접한 칸에 앉은 좋아하는 학생의 수
            for k in range(4):
                r, c = i+dr[k], j+dc[k]
                if 0 <= r < N and 0 <= c < N:
                    if seats[r][c] in likes[s]:
                        cnt += 1
            if cnt > 0:
                res += 10 ** (cnt-1)

    return res


def solution(students, likes):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    seats = [[None for _ in range(N)] for _ in range(N)]

    for s in students:
        max_like = 0 # 인접한 칸에 좋아하는 학생이 가장 많이 앉은 경우의 학생 수
        max_like_seat = [] # max_like를 가지는 칸의 좌표 저장
        
        # 좋아하는 학생이 있는지의 여부를 나타내는 2차원 배열을 만들어 사용
        tmp_seat = [[0 for _ in range(N)]for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if seats[i][j] in likes[s]:
                    tmp_seat[i][j] = 1 # 좋아하는 학생이 앉아있으면 1

        # 1번 단계
        for i in range(N):
            for j in range(N):
                if seats[i][j] != None: # 빈자리가 아니면 넘어가기
                    continue
                cnt = 0 # 인접하는 칸에 앉은 좋아하는 학생의 수
                for k in range(4):
                    tmp_r, tmp_c = i+dr[k], j+dc[k]
                    if 0 <= tmp_r < N and 0 <= tmp_c < N:
                        cnt += tmp_seat[tmp_r][tmp_c]
    
                # 최대 인접 좋아하는 학생 수 갱신
                if cnt > max_like:
                    max_like = cnt
                    max_like_seat = [(i, j)]
                elif cnt == max_like:
                    max_like_seat.append((i, j))
        
        if len(max_like_seat) == 1:
            r, c = max_like_seat[0]
            seats[r][c] = s
            continue
        else:
            # 2번 단계
            max_empty = 0 # 인접한 자리 중 최대로 빈 자리 수
            max_empty_seat = [] # 최대값을 가지는 자리의 좌표를 저장
            for candidate in max_like_seat:
                empty_cnt = 0
                r, c = candidate
                for k in range(4):
                    tmp_r, tmp_c = r+dr[k], c+dc[k]
                    if 0 <= tmp_r < N and 0 <= tmp_c < N:
                        if seats[tmp_r][tmp_c] == None:
                            empty_cnt += 1
                # 최대 빈 자리값 갱신
                if empty_cnt > max_empty:
                    max_empty = empty_cnt
                    max_empty_seat = [(r, c)]
                elif empty_cnt == max_empty:
                    max_empty_seat.append((r, c))

            if len(max_empty_seat) == 1:
                r, c = max_empty_seat[0]
                seats[r][c] = s
                continue

            else:
                # 3번 단계
                r, c = max_empty_seat[0]
                seats[r][c] = s

    score = satisfaction(likes, seats)
    return score

print(solution(students, likes))