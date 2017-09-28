try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('/path/to/file', 'r') as f:
    print(f.read())

f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')



#stringio. byteio
from io import StringIO
f = StringIO()
f.write("hello")
f.write("world!")
print(f.getvalue())


 from io import BytesIO
 f = BytesIO()
 f.write("中文".encode(encoding='utf-8'))
 print(f.getvalue())