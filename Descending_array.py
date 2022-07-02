n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if(i==(n-1)):
        break
    if(a[i]<=a[i+1]):
        c+=1
if(c>0):
    print("no")
else:
    print("yes")