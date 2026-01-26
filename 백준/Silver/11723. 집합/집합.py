import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    N = sys.stdin.readline().split()

    if N[0] == 'add':
        S.add(int(N[1]))

    elif N[0] == 'remove':
        S.discard(int(N[1]))

    elif N[0] == 'check':
        if int(N[1]) in S:
            print(1)
        else:
            print(0)

    elif N[0] == 'toggle':
        if int(N[1]) in S:
            S.discard(int(N[1]))
        else:
            S.add(int(N[1]))

    elif N[0] == 'all':
        S = set(i for i in range(1,21))
    else:
        S = set()