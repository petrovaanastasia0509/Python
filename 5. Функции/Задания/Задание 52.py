def is_perf(num):
    summ=0
    for i in range(1,num):
        if num % i == 0:
            summ+=i
    if summ==num:
        return True
    else:
        return False
n=int(input())
num=1
count=0
while count < n:
    if is_perf(num):
        count+=1
        print(num,end=' ')
    num+=1

