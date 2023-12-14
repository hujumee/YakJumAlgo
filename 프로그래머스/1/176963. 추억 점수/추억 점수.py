def solution(name, yearning, photo):
    answer = []
    
    score_dic = {}
    for i in range(len(name)):
        score_dic[name[i]] = yearning[i]
    
    for elem in photo:
        score = 0
        for p in elem:
            if p in name:
                score = score + score_dic[p]
        answer.append(score)
    
    return answer