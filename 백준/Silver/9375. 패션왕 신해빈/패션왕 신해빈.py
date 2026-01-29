import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    T = int(input())

    clothes = {}
    ans = 1

    for _ in range(T):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1

    for i in clothes.values():
        ans = ans * (i + 1)
    print(ans - 1)