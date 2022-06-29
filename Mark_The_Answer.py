n,x=map(int,input().split())
arr=list(map(int,input().split()))
skip=c=0
for i in range(n):
    if(arr[i]<=x):
        c+=1
    elif arr[i]>x:
        skip+=1
    if skip==2:
        break
    
print(c)
    
