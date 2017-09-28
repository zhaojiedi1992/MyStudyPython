class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("must be int")
        if value < 0 or value > 100:
            raise ValueError("between 0-100")
        self._score = value 