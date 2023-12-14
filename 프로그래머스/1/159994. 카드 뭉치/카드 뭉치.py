def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    wordlist = cards1 + cards2
    i1 = 0
    i2 = len(cards1)
    
    for word in goal:
        i = wordlist.index(word)
        if i == i1:
            i1 = i1 + 1
        elif i == i2:
            i2 = i2 + 1
        else:
            answer = 'No'
            break
        
    return answer