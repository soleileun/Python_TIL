import sys
N = int(input())
data = []
for i in range(N):
	data.append(int(sys.stdin.readline())) 
data.sort()
ans = ''
for  d in data:
    ans += str(d) + '\n'
print