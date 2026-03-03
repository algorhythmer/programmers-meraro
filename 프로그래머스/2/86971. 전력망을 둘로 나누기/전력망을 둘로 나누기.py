from collections import *

def solution(n, wires):
    graph = defaultdict(list)    
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    answer = len(wires) + 1
    for x, y in wires:
        answer = min(answer, abs(bfs(x, y, graph) - bfs(y, x, graph)))
    return answer

def bfs(x, y, graph):
    n = 0
    queue = deque([x])
    visited = set([x])
    
    while queue:
        n += 1
        curr = queue.popleft()
        for i in graph[curr]:
            if i != y and not i in visited:
                queue.append(i)
                visited.add(i)
    return n