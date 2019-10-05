# allowed chars are alpha, numeric, '-' (dash), '.' (dot), '_' (underscore)
# remove the item if disallowed chars

import re

list1=["abc","abc1","123","_abc","ab.9i","-","abc$"]

pattern=re.compile("[a-zA-Z0-9_.-]+")

for element in list1:

    if list([element])==pattern.findall(element):
        print(element)
