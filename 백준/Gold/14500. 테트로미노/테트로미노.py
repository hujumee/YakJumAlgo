import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    table[i] = tmp

# 테트로미노로 가능한 최대합 찾기
def getMaxSum(m_sum, table, tet_arr):
    for i in range(N):
        for j in range(M):
            r1, c1 = i, j
            r2, c2 = i+tet_arr[0][0], j+tet_arr[0][1]
            r3, c3 = i+tet_arr[1][0], j+tet_arr[1][1]
            r4, c4 = i+tet_arr[2][0], j+tet_arr[2][1]
            if all(0 <= r < N for r in [r1, r2, r3, r4]) and all(0 <= c < M for c in [c1, c2, c3, c4]):
                tmp_sum = table[r1][c1] + table[r2][c2] + table[r3][c3] + table[r4][c4]
                m_sum = max(m_sum, tmp_sum)
    return m_sum

def solution(table):
    t1_1 = [[0,1], [0,2], [0,3]]
    t1_2 = [[1,0], [2,0], [3,0]]
    t2 = [[0,1], [1,0], [1,1]]
    t3_1_1 = [[1,0], [2,0], [2,1]]
    t3_1_2 = [[1,0], [2,0], [2,-1]]
    t3_2_1 = [[0,1], [0,2], [1,0]]
    t3_2_2 = [[0,1], [0,2], [1,2]]
    t3_3_1 = [[0,1], [1,1], [2,1]]
    t3_3_2 = [[1,0], [2,0], [0,1]]
    t3_4_1 = [[0,1], [0,2], [-1,2]]
    t3_4_2 = [[1,0], [1,1], [1,2]]
    t4_1 = [[1,0], [1,1], [2,1]]
    t4_2 = [[1,0], [1,-1], [2,-1]]
    t4_3 = [[0,-1], [1,-1], [1,-2]]
    t4_4 = [[0,1], [1,1], [1,2]]
    t5_1 = [[1,0], [1,1], [1,-1]]
    t5_2 = [[1,0], [1,1], [2,0]]
    t5_3 = [[0,-1], [1,0], [0,1]]
    t5_4 = [[0,1], [-1,1], [1,1]]

    tet_arrs = [t1_1, t1_2, t2, t3_1_1, t3_1_2, t3_2_1, t3_2_2, t3_3_1, t3_3_2, t3_4_1, t3_4_2, t4_1, t4_2, t4_3, t4_4, t5_1, t5_2, t5_3, t5_4]
    m_sum = 0
    for arr in tet_arrs:
        m_sum = getMaxSum(m_sum, table, arr)
    return m_sum

print(solution(table))