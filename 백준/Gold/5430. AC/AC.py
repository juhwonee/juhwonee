import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr2 = input().strip()[1:-1].split(',')
    arr = deque(arr2)

    flag = 0
    rever = 0

    if n == 0:
        arr = deque()

    for i in p:
        if i == 'R':
            rever = not rever
        elif i == 'D':
            if arr:
                if rever == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                flag = 1
                print('error')
                break

    if flag == 0:
        if len(arr) == 0:
            print('[]')
        else:
            if rever == 1:
                arr.reverse()
            print('[', end='')
            for i in range (len(arr)-1):
                print(arr[i], end=',')
            print(arr[-1], end='')
            print(']')