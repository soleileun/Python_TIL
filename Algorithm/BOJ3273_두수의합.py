n = int(input())
a = list(map(int,input().split()))
target = int(input())
ans = 0
a = sorted(a)
l = 0
r = len(a)-1
while(l<r):
    tmp = a[l]+ a[r]
    if tmp == target:
        ans = ans+1
        l = l+1
    elif tmp < target :
        l = l+1
    else:
        r = r-1
print(ans)