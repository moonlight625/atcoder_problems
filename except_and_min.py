from collections import deque

n,qn = map(int, input().split())
b = list(map(int, input().split()))

for _ in range(qn):
    m = int(input())
    x = list(map(int, input().split()))
    l = []
    for i in range(1,n+1):
        if i not in x:
            l.append(b[i-1])
    print(min(l))