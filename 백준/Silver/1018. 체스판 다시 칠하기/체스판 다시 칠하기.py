N, M = map(int, input().split())
arr = []
result = []

for i in range(N):
    arr.append(input())

for n in range(N-7):
    for m in range(M-7):
        B = 0
        W = 0

        if (n+m) % 2 == 0:
            for i in range(n, n+8):
                for j in range(m, m+8):
                    if (i+j) % 2 == 0:
                        if arr[i][j] != 'B':
                            B += 1
                        if arr[i][j] != 'W':
                            W += 1
                    else:
                        if arr[i][j] != 'W':
                            B += 1
                        if arr[i][j] != 'B':
                            W += 1

        else:
            for i in range(n, n+8):
                for j in range(m, m+8):
                    if (i+j) % 2 == 1:
                        if arr[i][j] != 'B':
                            B += 1
                        if arr[i][j] != 'W':
                            W += 1
                    else:
                        if arr[i][j] != 'W':
                            B += 1
                        if arr[i][j] != 'B':
                            W += 1

        result.append(min(B, W))
print(min(result))