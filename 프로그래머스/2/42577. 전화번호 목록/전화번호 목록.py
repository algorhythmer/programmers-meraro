from collections import *

def solution(phone_book):
    answer = True
    nums = set()
    
    phone_book.sort(key=len)
    for num in phone_book:
        nums.add(num)
    
    for num in phone_book:
        for i in range(len(num)):
            if num[:i] in nums:
                return False
    
    return answer

