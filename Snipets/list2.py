# allowed chars are alpha, numeric, '-' (dash), '.' (dot), '_' (underscore)
# remove the item if disallowed chars

import re

def refineList(list1):
    pattern=re.compile("[a-zA-Z0-9_.-]+")

    for element in list1:
        if list([element])!=pattern.findall(element):
            list1.remove(element)

    return list1

list1=["abc","abc1","123","_abc","ab.9i","-","abc$"]
list2=refineList(list1)
for element in list2:
    print(element)