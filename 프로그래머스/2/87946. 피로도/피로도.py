def solution(k, dungeons):
    answer = 0
    l = len(dungeons)
    visited = [False] * l
    
    def visit(curr, cnt):
        nonlocal answer 
        answer = max(answer, cnt)
        
        for i, (x, y) in enumerate(dungeons):
            if visited[i] or x > curr: continue
            visited[i] = True
            visit(curr-y, cnt+1)
            visited[i] =False
        
    visit(k, 0)
    return answer

