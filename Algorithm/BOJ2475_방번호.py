import math

n = input()
a = [0]*10  
for i in n:
    a[int(i)] = a[int(i)] + 1
m = -1
idx = -1
for i in range(0,len(a)):
    if i ==6 or i ==9:
        tmp = math.ceil((a[6]+a[9])/2)
    else:
        if(m<a[i]):
            m = a[i]
            idx = i
print( tmp if tmp>m else m)
    