n=int(input())
dg=0
summ=0
while n > 0:
    dg=n%10
    summ+=dg
    n=n//10
print(summ)
