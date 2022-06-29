m=int(input())
tar=list(map(int,input().split()))
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if i not in tar:
        c=1
        break
if(c==1):
    print(False)
else:
    print(True)
            