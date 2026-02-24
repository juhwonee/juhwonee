import sys
input = sys.stdin.readline

N = int(input())

result = []

for _ in range(N):
    s = input().strip()
    sum_num = 0
    for i in s:
        if '0' <= i <= '9':
           sum_num += int(i)

    result.append((len(s), sum_num, s))
result.sort()
for i in result:
    print(i[2])