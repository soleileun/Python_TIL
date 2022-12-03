n = int(input())
x = 2*n -1

for i in range(0,n) : 
    print(" "*i + "*"*(x-i*2))
    
for i in range(n-2,-1,-1) : 
    print(" "*i + "*"*(x-i*2))

