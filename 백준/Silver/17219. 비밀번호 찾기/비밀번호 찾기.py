import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
for i in range(N):
    site, pw = map(str, input().strip().split())
    dic[site] = pw

for i in range(M):
    site = input().strip()
    print(dic[site])