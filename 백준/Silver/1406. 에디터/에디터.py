import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

M = int(input())

for _ in range(M):
    C = input().split()

    if C[0] == 'L':
        if left:
            right.append(left.pop())
    elif C[0] == 'D':
        if right:
            left.append(right.pop())
    elif C[0] == 'B':
        if left:
            left.pop()
    else:  # P x
        left.append(C[1])

while right:
    left.append(right.pop())

print(''.join(left))