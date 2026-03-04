from collections import *

def solution(n, wires):
    answer = n
    graph = defaultdict(list)
    visited = [False] * (n+1)
    
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    def dfs(x, y):
        last = False
        cnt = 1
        visited[x] = True
        for nxt in graph[x]:
            if nxt==y or visited[nxt]: continue
            cnt += dfs(nxt, y)
        visited[x] = False
        
        return cnt
    for x, y in wires:
        answer = min(answer, abs(dfs(x, y)-dfs(y, x)))
    
    return answer
    