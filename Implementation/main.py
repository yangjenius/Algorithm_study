n = int(input())
m = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
num = n * n
i = 0
x, y = 0, 0

while True:
  graph[x][y] = num
  nx = x + dx[i]
  ny = y + dy[i]
  
  if nx >= n or ny >= n or graph[nx][ny] != 0 or nx <= -1 or ny <= -1:
    i += 1
    if i == 4:
      i = 0
    continue

  x, y = nx, ny
  num -= 1
  if num == 1:
    break

graph[x][y] = 1


for i in range(n):
  for j in range(n):
    if graph[i][j] == m:
      k, w = i+1, j+1

  print(*graph[i])


print(k,w)