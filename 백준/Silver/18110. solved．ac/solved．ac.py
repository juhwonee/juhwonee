import sys
input = sys.stdin.readline
def round2(num):
    if float(num) - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())
if N == 0:
    print(0)
else:
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()

    cut = round2(N*0.15)

    arr2 = arr[cut:N-cut]
    avg = sum(arr2) / len(arr2)
    print(round2(avg))