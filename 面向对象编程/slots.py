class Student(object):
    #__slots__  = ('name','age')
    pass

s= Student()
from types import MethodType
def set_age(self,age):
    self.age=age
s.set_age = MethodType(set_age,s)
#print(s.set_age)
s.set_age(25)
print(s.age)