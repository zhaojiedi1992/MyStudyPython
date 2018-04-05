import math

def isPrime(n):#质数判断

        if n == 1:
                return False
        elif n < 4:
                return True
        elif n & 1 == 0:
                return False
        elif n < 9:
                return True
        elif n %3 == 0:
                return False
        else:
                r = math.floor(math.sqrt(n))
                f = 5
                while f <= r:
                        if n % f == 0:
                                return False
                        if n %(f+2) == 0:
                                return False
                        f += 6
                return True

def prime(n):
    x=1
    m=n
    while n>0:#循环判断
        #if n%10000 == 0:
            #print(n)
        x=x+1
        if isPrime(x):
            n=n-1
            if n%10000 == 0:
                print(n)
            if n==0:
                print ("第"+str(m)+"个质数是："+str(x))


prime(522048)