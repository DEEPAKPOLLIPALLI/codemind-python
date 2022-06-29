n,l=map(int,input().split())
if(n>=1 and l>=1 and n<=1000 and l<=1000):
    for i in range(1,l+1):
        t=n*i
        if(i%2!=0):
            print(n,'x',i,'=',t)
