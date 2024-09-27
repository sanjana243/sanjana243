import math
from collections import Counter
def primefactor(num):
    factor=[]
    while num%2==0:
        factor.append(2)
        num//=2
        
    for i in range(3, int(math.sqrt(num))+1,2):
        while num%i==0:
            factor.append(i)
            num//=i
            
    if num >2:
        factor.append(num)
    return Counter(factor)
    
def calcsum(arr,num):
    if not arr:
        return -1
    factorcount = primefactor(num)
    totalsum=0
    n=len(arr)
    
    for prime,exponent in factorcount.items():
        if prime < n:
            totalsum += exponent*arr[prime]
        else:
            return 0
    return totalsum
    
    
n=int(input())
arr=list(map(int,input().split()))
num=int(input())
result=calcsum(arr,num)
print(result)
