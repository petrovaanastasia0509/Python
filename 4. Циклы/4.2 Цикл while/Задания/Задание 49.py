summ=0
k=0
while (n:=int(input())) != 0:
    summ+=n
    k+=1
if k==0:
    print(0)
else:
    print(summ/k)

