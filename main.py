from random import randint
import math
n=int(input())
ff=[0]*n
k=3
for i in range(0,n):
    ff[i]=int(input())
ff.sort()
a=ff[n-1]
b=ff[n-2]
c=ff[n-k]
while (a>(b+c)) or (b>(a+c)) or (c>(a+b)) and (k!=n):
    k+=1
    c=ff[n-k]
if (k!=n):
    p=(a+b+c)/2
    print (math.sqrt(p*(p-a)*(p-b)*(p-c)))
else:
    print("no")






