import sys
input = sys.stdin.readline

T = int(input())

arr = [1,1,1,2,2,3,4,5,7,9] + [0] * 91
for i in range(10, 101):
    arr[i] = arr[i-2] + arr[i-3]

for _ in range(T):
    N = int(input())
    print(arr[N-1])