import sys
from collections import deque

N = int(input())
board = [ [ 0 for col in range( int(N) ) ]  for row in range(int(N))]
visit = [ [ False for col in range( int(N) ) ]  for row in range(int(N))]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = []
for i in range(N):
    cmd = sys.stdin.readline();
    for j in range(N):
        if(cmd[j] == 'R') :
            board[i][j] = 1
        elif(cmd[j] == 'G') :
            board[i][j] = 2
        else:
            board[i][j] = 3    
cntR = 0
cntG = 0
cntB = 0
q = deque()


for i in range(N):
    for j in range(N):
        if (visit[i][j] == False) :
            target = board[i][j]
            if(board[i][j] == 1):
                cntR +=1
            elif(board[i][j] == 2):
                cntG +=1
            else:
                cntB +=1
            visit[i][j] = True
            q.append((i,j))
            while(len(q) > 0) :
                temp = q.popleft()
                x,y = temp[0],temp[1]
                for dir in range(4):
                    tx = x+dx[dir]
                    ty = y+dy[dir]
                    if (tx<0 or ty <0 or tx>=N or ty>=N) : continue
                    if (visit[tx][ty] == True or board[tx][ty] != target ) : continue 
                    visit[tx][ty] = True
                    q.append((tx,ty))

ans.append(cntR+cntG+cntB)

visit = [ [ False for col in range( int(N) ) ]  for row in range(int(N))]
for i in range(N):
    for j in range(N):
        if(board[i][j] == 2):
            board[i][j] = 1

cntR = 0
cntB = 0
q = deque()
                    
for i in range(N):
    for j in range(N):
        if (visit[i][j] == False) :
            target = board[i][j]
            if(board[i][j] == 1):
                cntR +=1
            else:
                cntB +=1
            visit[i][j] = True
            q.append((i,j))
            while(len(q) > 0) :
                temp = q.popleft()
                x,y = temp[0],temp[1]
                for dir in range(4):
                    tx = x+dx[dir]
                    ty = y+dy[dir]
                    if (tx<0 or ty <0 or tx>=N or ty>=N) : continue
                    if (visit[tx][ty] == True or board[tx][ty] != target ) : continue 
                    visit[tx][ty] = True
                    q.append((tx,ty))


ans.append(cntR + cntB) 
print(ans[0] ,ans[1] )
                
