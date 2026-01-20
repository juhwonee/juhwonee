N = int(input())
people = [[0, 0] for _ in  range(N)]

for i in range(N):
    people[i][0], people[i][1] = map(int, input().split())

for j in range(N):
    rank = 1
    for k in range(N):

        if people[j][0] < people[k][0] and people[j][1] < people[k][1]:
            rank += 1

    print(rank, end=' ')