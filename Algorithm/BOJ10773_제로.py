n = int(input())
stck = []
for i in range(n):
    x = int(input())
    if(x == 0):
        stck.pop()
    else:
        stck.append(x)
sum = 0
for i in stck:
    sum += int(i)
print(sum)