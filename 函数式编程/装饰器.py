import datetime
def now1():
     print('2015-3-25')

def log(func):
    def wrapper(*args,**kw):
        print("call %s:" %func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now2():
    print('2015-3-25')

now1()
print("="*100)
now2()