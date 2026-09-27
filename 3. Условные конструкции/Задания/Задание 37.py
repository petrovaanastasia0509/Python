n=int(input())
last_dg=n%10
if last_dg==1 and n % 100 != 11:
    print('гриб')
elif 2<=last_dg<=4 and (n % 100 < 10 or n % 100 >= 20):
    print('гриба')
else:
    print('грибов')
