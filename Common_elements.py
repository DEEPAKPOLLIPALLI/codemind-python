n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
p=0
q=0
for i in a:
    if(i in b and i not in c):
        c+=[i]
        p+=1
for j in c:
    print(j,end=' ')