# import math
import sys
N = int(sys.stdin.readline())
# print(  math.ceil(math.sqrt(N)))
# python 부동소수점을 사용하는 제곱근연산의 문제로 틀림 
l,r = 0,N

while l<=r:
    mid = (l+r)//2
    if (mid**2) < N:
        l = mid + 1
    else:
        r = mid - 1
print(l)  