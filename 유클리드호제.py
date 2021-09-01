import math
a,b = map(int,input().split())
temp = 0;
result = math.gcd(a,b)
print(int(a*b/result))