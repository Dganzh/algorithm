

def gcd(a,b):
    '''
    Greatest Common Divisor
    辗转相除法求 a和b的最大公约数
    若|a|<|b|则a%b=a
    即小数对大数（指绝对值大小）取余仍是小数
    '''
    while b!=0:
        a,b=b,a%b
    return a
#print(gcd(319,377))  #29


#求素数

#构造序列(只需奇数即可)
def _odd_iter():
    n=1
    while True:
        n+=2
        yield n
#定义筛选函数
def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)


for n in primes():
    if n<100:
        print(n)
    else:
        break

