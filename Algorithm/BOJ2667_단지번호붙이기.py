import sys
from collections import deque
n = int(input())
board = [[ 0 for _ in range(n)] for _ in range(n)]
visit = [[ False for _ in range(n)] for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(n):
    cmd = sys.stdin.readline()
    for j in range(n):
        board[i][j] = int(cmd[j])
ans = []
total = 0
q=deque()
for i in range(n) :
    for j in range(n) :
        if( board[i][j] == 0 or visit[i][j] == True) : continue
        q.append((i,j)) 
        total +=1
        visit[i][j] = True
        home = 1
        while(len(q)>0):
            x,y = q.pop()
            for dir in range(4):
                tx = x+dx[dir]
                ty = y+dy[dir]
                if(tx<0 or ty<0 or tx>=n or ty>=n ) : continue
                if(board[tx][ty] == 0 or visit[tx][ty] == True) : continue
                q.append((tx,ty))
                visit[tx][ty] = True
                home +=1
        ans.append(home)

print(total)
ans.sort()
for a in ans:
    print(a)
    