a = 20
lis = []

for i in range(a):
    if (len(lis) !=20):
        lis.append(int(input()))
lis.sort()
lis.reverse()
for i in lis:
    if (i%3 ==0):
        print(i)