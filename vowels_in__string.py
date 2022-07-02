s=input()
arr=[]
for i in s:
    if i in "aeiouAEIOU":
        if i not in arr:
            arr.append(i)
if len(arr)!=0:
    print(*arr)
else:
    print(-1)