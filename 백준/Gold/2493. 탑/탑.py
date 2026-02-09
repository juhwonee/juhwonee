import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))

ans = [0] * N
height = []
index = []

for i in range(N):
    while height and height[-1] < T[i]:  # 6<9, 9>5, 5<7, 7>4
        height.pop()  # 6제거 -> 5제거
        index.pop()   # 1제거 -> 3제거

    if height:
        ans[i] = index[-1] # [0,0,2,2,4]
    else:
        ans[i] = 0

    height.append(T[i])  # [6] -> [9] -> [9,5] -> [9,7] -> [9,7,4]
    index.append(i+1)    # [1] -> [2] -> [2,3] -> [2,4] -> [2,4,5]

for i in range(len(ans)-1):
    print(ans[i], end=' ')
print(ans[-1])