lis = []

for i in range(1,21):
    lis.append("17 * "+ str(i) + " = " + str(17*i)  )
lis = lis[::-1]
for i in range(len(lis)):
    print(lis[i])