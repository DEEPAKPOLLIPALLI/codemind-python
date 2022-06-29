s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
x=0
if len(a)==len(b):
    for ch in a:
        for char in b:
            if ch not in b:
                x=1
                break
    if x==0:
        print("True")
    else:
        print("False")
else:
    print("False")