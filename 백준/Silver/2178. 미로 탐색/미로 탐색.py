N, M = map(int, input().split())

matrix = []
for _ in range(N):
    row = list(map(int, input().strip()))
    matrix.append(row)


def BFS(x,y):
    queue = []
    start_matrix = (x, y)
    queue.append(start_matrix)

    while queue:
        x, y = queue.pop(0)

        if x == N-1 and y == M-1:
            return matrix[x][y]

        if x - 1 >= 0 and matrix[x - 1][y] == 1:
            matrix[x - 1][y] = matrix[x][y] + 1
            queue.append((x - 1, y))

        if x + 1 < N and matrix[x + 1][y] == 1:
            matrix[x + 1][y] = matrix[x][y] + 1
            queue.append((x + 1, y))

        if y - 1 >= 0 and matrix[x][y - 1] == 1:
            matrix[x][y - 1] = matrix[x][y] + 1
            queue.append((x, y - 1))

        if y + 1 < M and matrix[x][y + 1] == 1:
            matrix[x][y + 1] = matrix[x][y] + 1
            queue.append((x, y + 1))

print(BFS(0,0))