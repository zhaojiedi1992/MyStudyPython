import itertools
natuals = itertools.count(1)
for n in natuals:
    print(n)

import itertools
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
    print(c)
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))   