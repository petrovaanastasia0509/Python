def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n=int(input())
a=2
count=0
while count < n:
    if is_prime(a):
        count+=1
        print(a, end=' ')
    a+=1

