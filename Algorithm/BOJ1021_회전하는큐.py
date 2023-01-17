from collections import deque
import sys


n,m = sys.stdin.readline().split()
x = sys.stdin.readline().split()
q = deque()

ans = 0

for i in range(1,int(n)+1):
    q.append(i)

for i in x :
    temp = q.index(int(i)) 
    if len(q)//2 > temp :
        q.rotate(-temp)
        ans += temp
    else:
        q.rotate(len(q) - temp)
        ans += len(q) - temp
    q.popleft()
print(ans)    

# # +면 뒤에있는걸 
# q.appendleft(q.pop())
# # - 음수면 
# q.append(q.popleft())






