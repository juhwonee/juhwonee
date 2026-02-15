n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

pic_cnt = 0
max_area = 0

def BFS(x,y):
    queue = []
    start_matrix = (x, y)
    queue.append(start_matrix)

    matrix[x][y] = 0
    area = 1

    while queue:
        x, y = queue.pop(0)

        if x - 1 >= 0 and matrix[x - 1][y] == 1:
            matrix[x - 1][y] = 0
            queue.append((x - 1, y))
            area += 1

        if x + 1 < n and matrix[x + 1][y] == 1:
            matrix[x + 1][y] = 0
            queue.append((x + 1, y))
            area += 1

        if y - 1 >= 0 and matrix[x][y - 1] == 1:
            matrix[x][y - 1] = 0
            queue.append((x, y - 1))
            area += 1

        if y + 1 < m and matrix[x][y + 1] == 1:
            matrix[x][y + 1] = 0
            queue.append((x, y + 1))
            area += 1

    return area

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            pic_cnt += 1
            area = BFS(i, j)
            if area > max_area:
                max_area = area
print(pic_cnt)
print(max_area)