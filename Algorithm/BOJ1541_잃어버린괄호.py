arr = input().split('-')
n = [] 
for i in arr:
    tmp = i.split('+')
    sum =0
    for j in tmp:
        sum += int(j)
    n.append(sum)
ans = n[0]
for i in range(1,len(n)):
    ans = ans - n[i]
print(ans) 
