import os 
print(os.name)

#print(os.uname())

print(os.environ)

print(os.path.abspath('.'))

print(os.path.split('/Users/michael/testdir/file.txt'))

print(os.path.splitext('/path/to/file.txt'))

a = [x for x in os.listdir('.') if os.path.isdir(x)]
print(a)

b=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(b)

import pickle
d=dict(name="zhaojiedi",age=24)

s = pickle.dumps(d)
print(s)

import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)



import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))