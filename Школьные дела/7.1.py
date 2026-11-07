def eccentricity(a, b):
    return ((a**2 - b**2)**0.5)/a
a,b=map(float,input().split())
print(eccentricity(a, b))