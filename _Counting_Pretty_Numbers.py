n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=0
    for k in range(a,b+1):
        while(k):
            j=k%10
            k=k/10
            break
        if(j==2 or j==3 or j==9):
            c+=1
    print(c)