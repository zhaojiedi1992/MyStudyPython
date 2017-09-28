
#变量可以指向函数
print(abs(-10))
f=abs
print(f(10))
#传入函数

def add(x,y,f):
    return f(x) + f(y)
print(add(1,-2,abs))

#map 
def normalize(name):
    return name[0:1].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#reduce
from functools import reduce

def prod(L):
    def mul(x,y):
        return  x * y 
    return reduce(mul,L)
print(prod([1,2,4,5,5]))

#map reduct 
from functools import reduce

def str2int(s):
    def fn(x,y):
        return 10 * x + y 
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))
print(str2int("12345"))

def str2float(s):
   p=s.split(".")
   s1=p[0]
   s2=p[1]
   return str2int(s1) + str2int(s2) / pow(10,len(s2))

print(str2float('123.4567'))   

#filter

def is_palindrome(n):
    s=str(n)
    length = len(s)
    for i in range(0,length//2):
        if s[i] !=s[-i-1] :
            return False
    return True

output = filter(is_palindrome, range(1, 1000))
print(list(output))
#sorted
c = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(c)