from collections import *

def solution(participant, completion):
    answer = ''
    names = defaultdict(int)
    for name in completion:
        names[name] += 1
    for name in participant: 
        if not name in names or names[name]==0:
            answer = name
        names[name] -= 1
    return answer