n=int(input())
arr=list(map(int,input().split()))
s=int(input())
c=0
for i in range(n):
    if(arr[i]==s):
        print(i)
        c+=1
        break
if(c==0):
    print(-1)