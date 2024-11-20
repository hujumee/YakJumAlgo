from collections import deque

def solution(edges):
    answer = [0] * 4

    # 해쉬 형태로 연결된 노드 저장
    graph = dict([])
    inDict, outDict = [0] * 1000002, [0] * 1000002 # 들어오는 간선, 나가는 간선 개수를 저장
    for edge in edges:
        start, end = edge
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
        inDict[end] += 1
        outDict[start] += 1
    
    # 시작 정점 찾기
    for key in graph.keys():
        if inDict[key] == 0 and outDict[key] >= 2:
            answer[0] = key
            break
    
    # 어떤 그래프인지 판단할 수 있는 정점이 나오기 전까지 dfs를 사용하여 순회
    stack = deque([])
    for end in graph[answer[0]]:
        stack.append((answer[0], end))
    graph.pop(answer[0])
    while stack:
        start, end = stack.pop()
        if outDict[end] == 0:
            # 나가는 간선이 없는 노드를 발견하면, 막대형 그래프 개수 +1
            answer[2] += 1
        elif outDict[end] == 2 and end != answer[0]:
            # 시작 정점이 아니고, 나가는 간선이 2개이면 8자형 그래프 개수 +1
            answer[3] += 1
        elif outDict[end] == 1 and end not in graph:
            # 나가는 간선이 1개인데, 해당 간선이 이미 stack에 들어와 graph에 없다면, 도넛형 그래프 개수 +1
            answer[1] += 1
        else:
            # 전부 다 해당하지 않으면, 연결된 간선을 stack에 넣고 graph에서 pop
            nodes = graph.pop(end)
            for node in nodes:
                stack.append((end, node))    

    return answer