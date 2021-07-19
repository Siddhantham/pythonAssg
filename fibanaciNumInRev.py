x , y = 1000,1001
lis = []
while y<5000:
    lis.append(y)
    x,y = y, x+y
    
lis = lis[::-1]
for i in range(len(lis)):
    print(lis[i])