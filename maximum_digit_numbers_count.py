n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if(i<0):
        i=i*(-1)
    c=0
    while(i):
        x=i%10
        i=i//10
        c+=1
    b.append(c)
k=max(b)
m=0
for j in a:
    temp=j
    if(j<0):
        j=j*(-1)
    d=0
    while(j):
        y=j%10
        j=j//10
        d+=1
    if(d==k):
        print(temp,end=' ')

        
        