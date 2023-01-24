target = int(input())
ans = 0
cnt = 0
for i in range(1,4294967296):
    if(target<=ans):
        if(target<ans):
            cnt -=1
        break
    ans += i
    cnt += 1
print(cnt)
