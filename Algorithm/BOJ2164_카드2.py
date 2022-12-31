from collections import deque

n = int(input())
q = deque()
for i in range(1,n+1):
    q.append(i)
while(len(q) > 1):
    q.popleft()
    if(len(q) == 1) : break
    x = q.popleft()
    q.append(x)
print(q[0])