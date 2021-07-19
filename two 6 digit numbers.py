a = input()
b = input()
lis = ''
for i in a:
    if( (i in b) and (i not in lis)):
        lis+=i+','
        
print(lis[:len(lis)-1])