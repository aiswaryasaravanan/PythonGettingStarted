# allowed chars are alpha, numeric, '-' (dash), '.' (dot), '_' (underscore)
# remove the item if disallowed chars

import re
import unittest

def refineList(list1):
    pattern=re.compile("[a-zA-Z0-9_.-]+")

    for element in list1:
        if list([element])!=pattern.findall(element):
            list1.remove(element)

    return list1

# list1=["abc","abc1","123","_abc","ab.9i","-","abc$"]
# list2=refineList(list1)
# for element in list2:
#     print(element)

class tesingClass(unittest.TestCase):
    def setUp(self): 
        pass
    def test(self): 
        self.assertEqual( refineList(["abc","123","a$a"]), ["abc","123"])
        self.assertEqual( refineList(["abc","abc1","123","_abc","ab.9i","-","abc$"]), ["abc","abc1","123","_abc","ab.9i","-"]) 
 

if __name__ == '__main__': 
    unittest.main() 