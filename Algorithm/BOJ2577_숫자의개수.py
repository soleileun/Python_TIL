tmp = 1
for i in range (0,3):
    n = int(input())
    tmp = tmp * n
ans = [0]*10    
num_str = f'{tmp}'
for x in (num_str):
    ans[int(x)] = ans[int(x)]+1
for n in ans:
    print(n)
