import sys

N = int(sys.stdin.readline())
temp = [ 0 ]
dp = [ 0 for _ in range(N+1)]
for i in range(N):
    temp.append(int(sys.stdin.readline()))

dp[1] = temp[1]
if( N > 1) : 
    dp[2] = temp[1] + temp[2]
for i in range(3,N+1):
    dp[i] = max( dp[i-2]+temp[i],dp[i-1],dp[i-3]+temp[i-1]+temp[i])

print(dp[N])

