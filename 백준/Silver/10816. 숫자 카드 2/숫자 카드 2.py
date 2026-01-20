import sys
input = sys.stdin.readline

N = int(input())
N_list = map(int, input().split())
M = int(input())
M_list = map(int, input().split())

dic = {}
for i in N_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in M_list:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')