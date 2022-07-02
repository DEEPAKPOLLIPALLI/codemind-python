n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
for i in a:
    if(i>=x and i<=y):
        c+=i
print(c)