from itertools import *

def solution(k, dungeons):
    l = len(dungeons)
    dp = [-1] * (1 << l)
    dp[0] = k
    answer = 0
    
    for visited_bits in range(1<<l):
        if dp[visited_bits] == -1 : continue
        
        curr = bin(visited_bits).count('1')
        answer = max(answer, curr)        
        
        for i in range(l):
            if visited_bits & (1<<i): continue
            if dp[visited_bits]  < dungeons[i][0]: continue
            n = visited_bits | (1 << i) 
            dp[n] = max(dp[n], dp[visited_bits] - dungeons[i][1])
    
    return answer