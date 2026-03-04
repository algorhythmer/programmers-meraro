from heapq import *
from collections import *

def solution(operations):
    valid = defaultdict(int)
    
    l = 0
    min_heap = []
    max_heap = []
    
    for op in operations:
        cmd, val = op.split()
        
        if cmd == 'I':
            num = int(val)
            heappush(min_heap, num)
            heappush(max_heap, -num)
            valid[num] += 1
            l += 1
        else:
            if l == 0: continue
            if val == '1':
                num = -heappop(max_heap)
                while valid[num]==0:
                    num = -heappop(max_heap)
                l -= 1
                valid[num] -= 1
            else:
                num = heappop(min_heap)
                while valid[num]==0:
                    num = heappop(min_heap)
                l -= 1
                valid[num] -= 1
                
    if l==0:
        return [0, 0]
        
    M = -heappop(max_heap)
    while valid[M] == 0:
        M = -heappop(max_heap)
    m = heappop(min_heap)
    while valid[m] == 0:
        m = heappop(min_heap)
    return [M, m]
