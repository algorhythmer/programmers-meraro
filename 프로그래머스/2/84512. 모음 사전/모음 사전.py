def solution(word):
    w = []
    answer = 0
    for i in range(10000):
        nextWord(w)
        answer += 1
        if word == ''.join(w):
            return answer
        
    return answer

def nextWord(word):
    if len(word) < 5:
        word.append('A')
        return
    
    def change(idx, word):
        if word[idx] == 'A':
            word[idx] = 'E'
        elif word[idx] == 'E':
            word[idx] = 'I'
        elif word[idx] == 'I':
            word[idx] = 'O'
        elif word[idx] == 'O':
            word[idx] = 'U'
        elif word[idx] == 'U':
            word.pop()
            change(idx-1, word)
    change(4, word)
            
        