maxx=-float("inf")
k=0
while (n:=int(input())) != 0:
    if maxx<n:
        maxx=n
        k=1
    elif maxx==n:
        k+=1
print(k)
