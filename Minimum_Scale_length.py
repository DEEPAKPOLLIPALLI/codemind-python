a=int(input())
arr=list(map(int,input().split()))
x=arr[0]
j=1
while j<a:
    if arr[j]%x==0:
        j+=1
    else:
        x=arr[j]%x
print(x)