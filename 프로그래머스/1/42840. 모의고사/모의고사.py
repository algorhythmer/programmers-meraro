def solution(answers):
    m1 = [1,2,3,4,5]
    m2 = [2,1,2,3,2,4,2,5]
    m3 = [3,1,2,4,5]
    
    result = [[0,0], [1,0], [2,0]]
    for i in range(len(answers)):
        ans = answers[i]
        if m1[i%5] == ans:
            result[0][1] += 1 
        if m2[i%8] == ans:
            result[1][1] += 1
        if m3[(i//2)%5] == ans:
            result[2][1] += 1
    M = max(result[0][1], result[1][1], result[2][1])
    answer = []
    for i, m in result:
        if M==m: answer.append(i+1)
    return answer