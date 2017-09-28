class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self._score = score

    def print_score(self):
        print('%s: %s' % (self.name, self._score))

a = Student("zhaojiedi",98)
#访问限制
print(a.name)
#print(a.score)
print(isinstance(a,Student))
hasattr(a,"name")
getattr(a,"name","abc")
setattr(a,"name","zhaojiedi2")
