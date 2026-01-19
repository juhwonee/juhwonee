N = int(input())
words = []

for _ in range(N):
    words.append(input())
words = list(set(words))

max_len = 0
for i in words:
    if len(i) > max_len:
        max_len = len(i)

for j in range(1, max_len+1):
    same_len = []
    for k in words:
        if len(k) == j:
            same_len.append(k)
    same_len.sort()

    for l in same_len:
        print(l)