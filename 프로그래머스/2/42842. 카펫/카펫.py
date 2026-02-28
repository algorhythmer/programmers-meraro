def solution(brown, yellow):
    answer = []
    n = (brown//2) + 2
    for x in range(1, (n+1)//2+1):
        y = n-x
        if (x-2)*(y-2) == yellow:
            return [y, x]
        
