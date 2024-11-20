# 주사위를 고르는 함수. 재귀를 사용.
# 원본 리스트, 몇번째 반복인지, 마지막으로 넣은 원소의 인덱스, 임시로 저장한 조합을 인자로 받음
def pick_dice(arr, i, j, temp): 
    global candidate
    n = len(arr)

    # 주사위 개수를 다 골랐으면 result에 append 후 리턴
    if i == n/2:
        answer = temp.copy()
        candidate.append(answer)
        return
    # 배열의 끝까지 도달했는데, n/2개를 고르지 않았을 경우, append하지 않고 리턴
    elif j == n-1:
        return

    # 주사위 개수를 고르지 않았으면, for문을 통해서 모든 경우의 수를 담아 pick 호출
    for k in range(j+1, n):
        temp.append(arr[k])
        pick_dice(arr, i+1, k, temp)
        temp.pop()
    return

# 어떤 한 사람의 주사위 조합을 받았을 때, 가능한 모든 주사위 값의 합을 구하는 함수. 재귀 사용.
# 모든 주사위 값의 합을 저장하는 리스트, 주사위 조합, 임시 점수, 몇번째 반복인지를 인자로 받음
def get_all_score(score_arr, dice, combi, score, n):
    # A, B의 모든 주사위를 돌았을 때, 결과값을 비교해서 game_result 값 변경
    if n == len(combi):
        score_arr.append(score)
        return
    
    picked_dice = dice[combi[n]]
    for i in range(6):
            score += picked_dice[i]
            get_all_score(score_arr, dice, combi, score, n+1)
            score -= picked_dice[i]
    return score_arr


candidate = [] # 가능한 주사위의 조합을 저장
game_result = [] # 각 주사위의 조합을 기반으로, 승리/패배/비김 경우의 수를 저장

def solution(dice):
    global candidate, game_result
    answer = []

    arr = [n for n in range(len(dice))]
    # 가능한 주사위 조합 모두 구하기
    pick_dice(arr, 0, -1, [])

    # 각 조합에 관하여, a와 b가 이기거나, 지거나, 비기는 모든 경우의 수 구하기
    for i in range(len(candidate)):
        combi = candidate[i]
        A, B = [], []
        for n in range(len(dice)):
            if n in combi:
                A.append(n)
            else:
                B.append(n)
        # 가능한 모든 주사위의 합을 구함
        A_score_arr = get_all_score([], dice, A, 0, 0)
        B_score_arr = get_all_score([], dice, B, 0, 0)
        A_score_arr.sort()
        B_score_arr.sort()

        # 모든 주사위의 합 경우의 수에 대하여 A가 이기거나, 비기거나, 지는 경우의 수를 game_result에 append
        result = [0, 0, 0]
        A_i, B_i = 0, 0
        score_len = len(A_score_arr)
        # 투포인터를 활용하여 이기고 지는 경우의 수 구함
        while 1:
            if A_score_arr[A_i] > B_score_arr[B_i]:
                if B_i != score_len-1:
                    result[0] += score_len-A_i
                    B_i += 1
                else:
                    result[0] += 1
                    A_i += 1
            elif A_score_arr[A_i] == B_score_arr[B_i]:
                result[1] += 1
                if A_i != score_len-1:
                    A_i += 1
                else:
                    B_i += 1
            elif A_score_arr[A_i] < B_score_arr[B_i]:
                if A_i != score_len-1:
                    result[2] += score_len - B_i
                    A_i += 1
                else:
                    result[2] += 1
                    B_i += 1
            if A_i == score_len-1 and B_i == score_len-1:
                break
        game_result.append(result)


    
    # 최다로 이기는 조합 찾기
    max, max_i = 0, 0 # 최대로 이긴 횟수, 최대로 이긴 횟수의 조합 인덱스
    for i in range(len(game_result)):
        win_result = game_result[i][0]
        # 최대를 찾았을 경우 max, max_i 갱신
        if win_result > max:
            max = win_result
            max_i = i
    for n in candidate[max_i]:
        answer.append(n+1)

    return answer