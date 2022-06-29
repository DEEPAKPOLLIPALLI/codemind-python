t=int(input())
for i in range(t):
    n=int(input())
    b=[]
    r=0
    while n>0:
        r=n%10
        b.append(r)
        n=n//10
    b.sort()
    c=0
    for i in range(len(b)):
        if i+1<len(b):
            if b[i+1]-b[i]==1:
                c=1
            else:
                c=2
                break
    if(c==2):
        print("NO")
    else:
        print("YES")
    
   