N, M = map(int, input().split())

dict = {}
for i in range(1, N+1):
    P = input()
    dict[i] = P
    dict[P] = i

for j in range(M):
    Q = input()
    if Q.isdigit():
        print(dict[int(Q)])
    else:
        print(dict[Q])