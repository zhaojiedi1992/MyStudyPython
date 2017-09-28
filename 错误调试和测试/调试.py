#使用断言
def foo(s):
    n=int(s)
    assert n!=0,'n is zero'
    return 10/n
def main():
    foo('0')

#使用日志记录
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#pdf方式