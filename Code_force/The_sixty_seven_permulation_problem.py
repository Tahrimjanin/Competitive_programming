# Formula = nPr = n! / (n-r)!
#n = Total number of objects
#r = Number of objects taken at a time

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    result = []
    for k in range(1, n + 1):
        result.extend([k, n + 2*k - 1, n + 2*k])
    print(*result)