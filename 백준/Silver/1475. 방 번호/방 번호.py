N = input()
cnt = [0 for _ in range(10)]

for i in range(len(N)):
    W = int(N[i])
    if W == 6 or W == 9:
        if cnt[6] <= cnt[9]:
            cnt[6] += 1
        else:
            cnt[9] += 1

    else:
        cnt[W] += 1

print(max(cnt))