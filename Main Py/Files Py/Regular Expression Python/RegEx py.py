# Regular EXP
import re
a="SASTRA UNIVERSITY"
re.split('UNI',a)

import re
a="sastra university university"
b=re.search('uni',a)   # serach() not  usable for 1 or more pattern
print(b.start())
print(b.end())
print(b.group())  # prints what pattern v r searching
c=re.findall('uni',a)  # Findall() 1 or more can also b counted
print(c)  # list data type

#re.search()
#re.findall() - can't find start(),end() , op as []
#re.finditer()

import re
a="sastra university university"
b=re.finditer('uni',a)
print(b)
for i in b:
  print((i.start(),i.end()))  # Match obj-type
  print(i.group())


import re
ph="+91-7999887690"
b=re.findall("\+91-\d{10}$",ph) # or  [0-9]+
if b:
  print("Valid number")
else:
  print("Not a valid number")
  
import re
txt="123 abc 456 def 789 ghi"
b=re.findall("\d+",txt)
print(tuple(b))

import re
txt="123 abc 456 def 789 ghi"
b=re.finditer("\d+",txt)
for i in b:
  print(i.group())
