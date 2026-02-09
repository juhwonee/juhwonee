N = int(input())
for _ in range(N):
    L = input()
    left = []
    right = []

    for i in L:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    while right:
        left.append(right.pop())

    for i in left:
        print(i, end='')
    print()