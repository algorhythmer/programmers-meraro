from heapq import *

def solution(jobs):
    jobs.sort()
    pq = []
    total = 0
    time = 0
    idx = 0
    while idx < len(jobs):
        t, s= jobs[idx]
        if t<=time:
            heappush(pq, (s, t, idx))
            idx += 1
            continue
        if pq:
            s, t, n = heappop(pq)
            time += s
            total += time-t
        else:
            time = t
    
    while pq:
        s, t, n = heappop(pq)
        time += s
        total += time-t
    
    return total // len(jobs)
    
    