N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

cnt = [0] * 257
for i in range(N):
    for j in range(M):
        cnt[ground[i][j]] += 1

ans = 10**18
h = 0

for height in range(257):
    remove = 0
    add = 0
    for k in range(257):
        if cnt[k] == 0:
            continue
        if k > height:
            remove += (k - height) * cnt[k]
        else:
            add += (height - k) * cnt[k]

    if B + remove < add:
        continue
    total = remove * 2 + add

    if total < ans or (total == ans and height > h):
        ans = total
        h = height

print(ans, h)
