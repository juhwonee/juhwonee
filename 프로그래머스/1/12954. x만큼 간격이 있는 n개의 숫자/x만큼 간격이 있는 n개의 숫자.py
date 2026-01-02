def solution(x, n):
    answer = []
    
    if x == 0:
        for i in range (n):
            answer.append(0)
    else:
        answer=[i for i in range(x, x*(n+1), x)]
    return answer