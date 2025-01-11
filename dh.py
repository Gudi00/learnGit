T = int(input())
if T < 1 or T > 10:
    exit()
answers = [-1] * T
for i in range(T):
    n = int(input())
    h = list(map(int, input().split()))
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))#ksjdfkjasdfhlkas

    min_values = [0] * n

    for o in range(100):
        min_values = [0] * n

        for j in range(n):
            for z in range(n):
                if h[j] < h[z]:
                    min_values[j] += 1

        check = True
        for z in range(n):
            if min_values[z] != t[z]:
                check = False
                break

        if check:
            answers[i] = o
            break
        else:
            for z in range(n):
                h[z] += a[z]

for answer in answers:
    print(answer)
