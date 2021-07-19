def altPrime(fir,sec):
    counter = 0
    for n in range(fir,sec):
        if (prime(n) == 1):
            if counter % 2 ==0:
                print(n, end=" ")
def prime(n):
    b = 0 
    for i in range(2,n//2+1):
        if (n %i==0):
            b =1 
            break
    if (b ==0):
        return 1
    else:
        return 0
    
fir = 200
sec = 500
altPrime(fir,sec)