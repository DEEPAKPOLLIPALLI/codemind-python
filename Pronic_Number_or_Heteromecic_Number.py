a=int(input())
c=0
for i in range(a):
    if i*(i+1)==a:
        c=1
        break
if c==1:
    print("YES")
else:
    print("NO")