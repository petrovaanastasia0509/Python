n=int(input())
maxx=n
k=0
while n != 0:
    if maxx<n:
        maxx=n
        k=1
    elif maxx==n:
        k+=1
    n=int(input())
print(k)
