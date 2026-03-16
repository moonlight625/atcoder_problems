s = input()
count = []
exist = []
dl = []
put = []

for i in range(len(s)):
    for j in range(len(exist)):
        if s[i] == exist[j]:
            count[j] += 1
            break
        # else:
        #     exist[j] = s[i]
        #     count[j] = 1
    else:
        exist.append(s[i])
        count.append(1)
            
max = max(count)

for i in range(len(exist)):
    if count[i] == max and exist[i] not in dl:
        dl.append(exist[i])
        # for t in s:
        #     if t != exist[i]:
        #         put.append(t)
            
for t in s:
    if t not in dl:
        put.append(t)
                
print(''.join(put))