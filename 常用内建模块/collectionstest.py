#namedtuple
from collections import namedtuple

Point = namedtuple("Point",['x','y'])

p = Point(1,2)
print(p.x ,p.y)

#deque

from collections import deque
q =deque(['a','b','c'])
q.append('x')
q.append('y')
print(q)

#defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'n/a')
dd["key1"]="key1"
print(dd["key1"])
print(dd["key2"])


#ordered dict 
from collections import OrderedDict
d = dict([('a',1),('b',2)])
od = OrderedDict(d)
print(od )

#counter 
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1