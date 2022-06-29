def pal(n):
    rev=temp=r=0
    temp=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if(temp==rev):
        return 1
    else:
        return 0
n=int(input())
rev=s=a=r=v=0
for i in range(n+1,10000):
    if(pal(i)==1):
        s=i
        v=i-n
        break
for j in range(n-1,0,-1):
    if(pal(j)==1):
        r=j
        a=n-j
        break
if(v>a):
    print(r)
elif(v==a):
    print(r,s)
else:
    print(s)
    
