import sys
input = sys.stdin.readline

first_line = input().split()
n = int(first_line[0])

arr = []

for i in first_line[1:]:
    arr.append(int(i[::-1]))

while len(arr) < n:
    nums = input().split()
    for j in nums:
        arr.append(int(j[::-1]))
arr.sort()

for num in arr:
    print(num)