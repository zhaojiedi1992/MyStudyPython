class Query(object):
    def __init__(self,name):
        self.name = name 
    def __enter__(self):
        print("begin")
        return self
 def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
def query(self):
    print("test query")

with Query("bob") as q:
    q.query()



from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')