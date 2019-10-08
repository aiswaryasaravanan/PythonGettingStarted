import unittest
from csvToCsv import getEmail, getName


class TesingClass(unittest.TestCase):

    def testEmail(self):
        actual = getEmail("Aiswarya", "Saravanan", "vmware.com")
        expected = "aiswaryasaravanan@vmware.com"
        self.assertEqual(actual, expected)
        self.assertEqual(getEmail("Ram", "Babu", "dbs.com"), "rambabu@dbs.com")
        self.assertEqual(getEmail("Ram", "", "dbs.com"), "ram@dbs.com")
        self.assertEqual(getEmail("S.Ram", "Babu", "dbs.com"), "s.rambabu@dbs.com")
        self.assertEqual(getEmail("Ram Babu", "S", "dbs.com"), "ram babus@dbs.com")

    def testName(self):
        self.assertEqual(getName("Aiswarya", "Saravanan"), "Aiswarya Saravanan")
        self.assertEqual(getName("Ram", "Babu"), "Ram Babu")
        self.assertEqual(getName("Ram", ""), "Ram ")
        self.assertEqual(getName("", ""), " ")


if __name__ == '__main__':
    unittest.main()
