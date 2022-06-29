import math
n=int(input())
p=list(map(int,input().split()))
v=0
c=0
r=0
k=0
b=[]
for i in range(n):
    if(i%2==0):
        v=v+p[i]
    else:
        r=r+p[i]
if(v>r):
    k=v-r
else:
    k=r-v
if(k%4==0):
    print("X")
else:
    print("Y")