import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]
data.sort()


sum_ = 0
for i in data:
    sum_ += i
print(round(sum_/N)) # 산술평균
print(data[N//2]) # 중앙값

# 최빈값
cnt = {}
for i in data: # -3,-2,-2,-1,-1
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1 # cnt[-3]=1, cnt[-2]=2, cnt[-1]=2

max_cnt = max(cnt.values()) # 2
freq = []
for key in cnt:
    if cnt[key] == max_cnt:
        freq.append(key)
freq.sort()

if len(freq) == 1:
    print(freq[0])
else:
    print(freq[1])

print(data[-1] - data[0]) # 범위