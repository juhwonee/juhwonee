N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def solution(idx, sum_arr):
    global cnt

    if idx == N:
        if sum_arr == S:
            cnt += 1
        return

    solution(idx+1, sum_arr+arr[idx]) # 선택O
    solution(idx+1, sum_arr) # 선택X

solution(0, 0)

if S == 0:
    cnt -= 1
print(cnt)