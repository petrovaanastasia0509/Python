p=1
old_n=0
maxp=0
while (n:=int(input())) != 0:
    if old_n ==n:
        p+=1
    if p > maxp:
        maxp=p
    if old_n != n:
        p=1
    old_n=n
print(maxp)