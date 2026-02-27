from itertools import *

def solution(numbers):
    answer = set()

    
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            n = int(''.join(p))
            print(n)
            if isPrime(n): answer.add(n)
    return len(answer)

def isPrime(num):
    if num <= 1: return False
    i = 2
    while i*i <= num:
        if num % i == 0: return False
        i += 1
    return True