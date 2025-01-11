n, m, k = list(map(int, input().split()))
a = []
c = []
ch = 0
for i in range(0, n):
    q = list(map(int, input().split()))
    a.append(q[0])
    c.append(q[1])
    print(a[i])
    print(c[i])


a = sorted(a)
for i in range(0, n - 1):
    if a[i] >= a[i + 1]:
        tmp = a[i]
        a[i] = a[i+1]
        a[i+1] = tmp
        tmp = c[i]
        c[i] = c[i+1]
        c[i+1] = tmp



    # max=c[0]
    # ind=0
    # for i in range(0, n):
    #     c[i]>max
    #     max=c[i]
    #     ind=i
    # if max>1:
    # if max(c)>1:
    #     ch += 1
    #     c[0]-=1
for i in range(0, n-1):
    if a[i+1] - a[i] >= k:
        c[i] -= 1
        ch+=1
ch+=1
i = 0
while c[i] == 0 and i<n:
    i+=1
if i +1 != n:
    ch+=1

for b in range(i, n-1):
   if a[b+1] - a[b] >= k and c[b+1]>0:


        c[b+1] -= 1
        ch+=1

print(ch)

