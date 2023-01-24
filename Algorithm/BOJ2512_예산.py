import sys
N = int(sys.stdin.readline())
temp = sys.stdin.readline().split()
sum = 0
group = []
for t in temp:
    group.append(int(t))
    sum += int(t)
M = int(sys.stdin.readline())
l,r = 0,M

if( sum <= M):
    print(max(group))
else: 
    while l <=r :
        mid = (l+r)//2
        total = 0
        for g in group:
            if(g<=mid):
                total+=g
            else:
                total+=mid
        if(total > M):
            r = mid -1
        else:
            l = mid +1
    print(r)
