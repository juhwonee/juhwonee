from collections import deque

C = int(input())

for _ in range(C):
    N, M = map(int, input().split()) # 6,0
    data = deque(map(int, input().split())) # 1,1,9,4,3,2
    score = 0

    while 1:
        if data[0] < max(data):
            data.append(data.popleft())
            M -= 1
            if M < 0:
                M = len(data)-1

        else:
            data.popleft()
            score += 1
            if M == 0:
                print(score)
                break
            else:
                M -= 1

