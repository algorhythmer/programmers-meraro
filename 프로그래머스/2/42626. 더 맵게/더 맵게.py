from heapq import *

def solution(scoville, K):
    answer = 0
    min_heap = []
    for s in scoville:
        heappush(min_heap, s)
    
    while len(min_heap)>1 and min_heap[0] < K:
        n1 = heappop(min_heap)
        n2 = heappop(min_heap)
        heappush(min_heap, n1 + 2*n2)
        answer += 1
    
    if min_heap[0] < K: return -1
        
    return answer