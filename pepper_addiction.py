# n, m = map(int, input().split())
# cl = list(map(int, input().split()))
# al =[] 
# bl = []
# pep = 0

# for i in range(n):
#     a, b = map(int, input().split())
#     al.append(a)
#     bl.append(b)
    
# for i in range(n):
#     if cl[al[i]-1] >= bl[i]:
#         pep += bl[i]
#         cl[al[i]-1] -= bl[i]
#     elif cl[al[i]-1] < bl[i]:
#         pep += cl[al[i]-1]
#         cl[al[i]-1] = 0

# print(pep)
     
n, m = map(int, input().split())
c = list(map(int, input().split()))   
pep = 0

for _ in range(n):
    a,b = map(int, input().split())
    if c[a-1] >= b:
        pep += b
        c[a-1] -= b
    else:
        pep += c[a-1]
        c[a-1] = 0

print(pep)