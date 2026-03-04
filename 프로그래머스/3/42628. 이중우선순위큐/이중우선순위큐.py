from heapq import *

def solution(operations):
    
    nums = []
    
    for op in operations:
        x, y= op.split()
        if x == 'I':
            nums.append(int(y))
        else:
            if not nums: continue
            
            if y == '1':
                for i in range(len(nums)):
                    nums[i] = -nums[i]
                heapify(nums)
                heappop(nums)
                for i in range(len(nums)):
                    nums[i] = -nums[i]
            else:
                heapify(nums)
                heappop(nums)
    if not nums:
        return [0, 0]
    heapify(nums)
    n1 = nums[0]
    for i in range(len(nums)):
        nums[i] = -nums[i]
    heapify(nums)
    n2 = -nums[0]
    
    return [n2, n1]