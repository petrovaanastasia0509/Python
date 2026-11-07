n=int(input())
tot=0
for i in range(n):
    a=int(input())
    if a % 121==43:
        tot+=a
print(tot)