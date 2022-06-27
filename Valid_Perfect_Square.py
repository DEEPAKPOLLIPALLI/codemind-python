t=int(input())
count=0
while t>0:
    n=int(input())
    count=0
    for i in range(1,n+1):
        if i*i==n:
            count+=1
    if count>0:
        print("True")
    else:
        print("False")
    t=t-1