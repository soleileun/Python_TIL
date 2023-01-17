from collections import deque
import sys
n = int(input())
for _ in range(n):
    cmd = sys.stdin.readline()
    x = int(input())
    temp = sys.stdin.readline()
    q = deque()
    arr = temp[1:-2].split(',')
    for i in arr :
        q.append(i)
    flag = True
    for c in cmd :
        if c == 'R':
            if(flag):
                flag = False
            else:
                flag = True
            
        elif c == 'D':
            if( x > 0):
                if(flag):
                    q.popleft()
                else:
                    q.pop()
            else:
                print("error")
                break
            x -=1
    
    if(flag == False):
        q.reverse()
    ans = "[" + ','.join(q) + "]"
    print("***", ans)

    