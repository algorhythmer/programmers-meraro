from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        k1 = heappop(scoville)
        k2 = heappop(scoville)
        heappush(scoville, k1 + 2*k2)
        answer += 1
        
    if scoville[0] < K: return -1
    
    return answer