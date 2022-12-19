n = int(input())
idx = 1
cnt = 0
stck = [0]
ans = []
flag = True
for i in range(n):
    x = int(input())
    top = stck[-1]
    cnt = 0
    if (top <= x):
        while(idx<=x):
            stck.append(idx)
            ans.append('+')
            idx +=1
            cnt +=1
    elif (top > x) :
        while(1):
            if(len(stck) > 0) :
                tmp = stck.pop()
                ans.append('-')
                if( tmp == x) : break
            else:  
                flag = False
                break
    top = stck[-1]
    if(flag == False) : break
    if(top == x):
        cnt +=1
        stck.pop()
        ans.append('-')
    if(cnt == 0 ) :
        flag = False
        break
if flag : 
    for i in ans:
        print(str(i), end='\n')
else : 
    print( "NO")            
    