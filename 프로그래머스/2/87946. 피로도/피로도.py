from itertools import *

def solution(k, dungeons):
    
    answer = 0
    for order in permutations(dungeons, len(dungeons)):
        n = 0
        m = k
        for x, y in order:
            if m >= x:
                m -= y
                n += 1
        answer = max(answer, n)
    
    return answer
