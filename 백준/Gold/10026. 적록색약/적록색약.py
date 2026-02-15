N = int(input())

matrix = []
for _ in range(N):
    row = list(input().strip())
    matrix.append(row)

def BFS(x,y,color,matrix):
    queue = []
    start_matrix = (x, y)
    queue.append(start_matrix)

    matrix[x][y] = '0'

    while queue:
        x, y = queue.pop(0)

        if x - 1 >= 0 and matrix[x - 1][y] == color:
            matrix[x - 1][y] = '0'
            queue.append((x - 1, y))

        if x + 1 < N and matrix[x + 1][y] == color:
            matrix[x + 1][y] = '0'
            queue.append((x + 1, y))

        if y - 1 >= 0 and matrix[x][y - 1] == color:
            matrix[x][y - 1] = '0'
            queue.append((x, y - 1))

        if y + 1 < N and matrix[x][y + 1] == color:
            matrix[x][y + 1] = '0'
            queue.append((x, y + 1))

normal = 0
matrix_normal = []
for i in range(N):
    row_normal = []
    for j in range(N):
        row_normal.append(matrix[i][j])
    matrix_normal.append(row_normal)

for i in range(N):
    for j in range(N):
        if matrix_normal[i][j] != '0':
            BFS(i,j,matrix_normal[i][j],matrix_normal)
            normal += 1
print(normal)

blind = 0
matrix_blind = []
for i in range(N):
    row_blind = []
    for j in range(N):
        row_blind.append(matrix[i][j])
    matrix_blind.append(row_blind)

for i in range(N):
    for j in range(N):
        if matrix_blind[i][j] == 'R':
            matrix_blind[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if matrix_blind[i][j] != '0':
            BFS(i,j,matrix_blind[i][j],matrix_blind)
            blind += 1
print(blind)