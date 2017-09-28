import re
b = re.match(r'^\d{3}-\d{3,8}','010-3243234') 
print(b)

c= re.split(r'\s+', 'a b   c')
print(c)


l = ["someone@gmail.com","bill.gates@microsoft.com"]
re_email = re.compile("(.*)?@.*?")
for it in l:
    b = re_email.match(it)
    #print(b)
    if b:
        print(b.group(1)) 
    else:
        print("not match ")