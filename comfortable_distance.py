n, l, r = map(int, input().split())
s = input()
count = 0

for i in range(n):
    for j in range(i,n):
        if s[i] == s[j] and l <= j - i <= r:
            count += 1
    
print(count)