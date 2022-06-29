def prime(a):
    c=0
    for i in range(1,a):
        if(a%i==0):
            c+=1
    if(c==1):
        return 1
    else:
        return 0
a=int(input())
c=0
for i in range(1,a):
    if(prime(i)==1):
        for j in range(1,a):
            if(prime(j)==1):
                if(i!=j):
                    if(i*j==a):
                        c=1
                        print(i,j)
                        break
        if(c==1):
            break
if(c==0):
    print("-1")
