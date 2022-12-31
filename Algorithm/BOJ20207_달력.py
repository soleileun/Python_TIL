import sys

n = int(input())

board = [ 0 for col in range(370)]
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(int(x), int(y)+1):
        board[i] +=1
max = -1
cnt = 0
sum = 0
for i in board:
    if i == 0 :
        if cnt > 0  and max != -1 :
            sum += cnt * max
            cnt = 0
            max = -1
    else:
        cnt += 1
        if max < i :
            max = i
            
print(sum)
        