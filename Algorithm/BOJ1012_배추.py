import sys
from collections import deque

T  = int(input())
dx = [-1,1,0,0]
dy = [0,0,1,-1]
answer = []

for t in range(T) :
    M,N,K = sys.stdin.readline().split()
    q = deque()
    board = [ [ 0 for col in range( int(M) ) ]  for row in range(int(N))]
    check = [ [ False for col in range( int(M) ) ]  for row in range(int(N))]
    for k in range(int(K)):
        x,y = sys.stdin.readline().split()
        board[int(y)][int(x)] = 1
    ans = 0
    for i in range(int(N)):
        for j in range(int(M)) :
            if board[i][j] == 0 or check[i][j] == True: continue
            q.append((i,j))
            ans +=1
            check[i][j] = True
            while(len(q) > 0 ):
                temp = q.popleft()
                x,y = temp[0],temp[1]
                for dir in range(4):
                    tx = x + dx[dir]
                    ty = y + dy[dir]
                    if(tx <0 or ty <0 or tx>= int(N) or ty >=int(M)):  continue
                    if(board[tx][ty] == 0 or check[tx][ty] == True): continue
                    check[tx][ty] = True
                    q.append((tx,ty))
    answer.append(ans)
for a in answer:
    print(a)
        
