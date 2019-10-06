import unittest
import list2

class tesingClass(unittest.TestCase):
    def setUp(self): 
        pass
    def test(self): 
        self.assertEqual( list2.refineList(["abc","123","a$a"]), ["abc","123"])
        self.assertEqual( list2.refineList(["abc","abc1","123","_abc","ab.9i","-","abc$"]), ["abc","abc1","123","_abc","ab.9i","-"]) 
 

if __name__ == '__main__': 
    unittest.main() 