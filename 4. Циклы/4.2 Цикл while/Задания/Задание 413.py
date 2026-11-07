max1=-float("inf")
p=0
max1_p=0
max2_p=0
while (n:=int(input())) != 0:
    p+=1
    if n>max1:
        max1=n
        max1_p=p
    if n>=max1:
        max2_p=p
print(max1_p, max2_p)