import unittest
import csvToCsv


class TesingClass(unittest.TestCase):

    def test(self):
        self.assertEqual(csvToCsv.suggestEmail(
            "Aiswarya", "Saravanan", "vmware.com"), "aiswaryasaravanan@vmware.com")


if __name__ == '__main__':
    unittest.main()
