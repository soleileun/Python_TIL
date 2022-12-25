n = int(input())
target = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]  #우 하 좌 상 
start = n//2 
board = [[0 for col in range(n)] for row in range(n)]
board[n//2][n//2] = 1
start_x = n//2
start_y = n//2
target_x = start_x
target_y = start_y
idx,cnt= 0,0
step = 3
start_x = n//2 - step//2
start_y = n//2 - step//2

if n == 1:
    target_x = 1
    target_y = 1
else:
    target_x +=1
    target_y +=1
for i in range(1,n*n):
    tmp_x = start_x + dx[idx]
    tmp_y = start_y + dy[idx]
    board[tmp_x][tmp_y] = i+1
    if i+1 == target:
        target_x = tmp_x +1
        target_y = tmp_y +1
    cnt +=1 
    start_x = tmp_x
    start_y = tmp_y
    if(cnt == (step // 2 * 2)):
        cnt = 0
        idx+=1
        if(idx == 4):
            idx = 0
            step +=2
            start_x = n//2 - step//2
            start_y = n//2 - step//2


for i in range(n):
    for j in range(n):
        print(board[i][j],end=" ")
    print()
print(target_x, target_y)
     