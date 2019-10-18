import consoleToCsv
import unittest
import random


class UnitTest(unittest.TestCase):

    def test_getRandomNumber(self):
        random.seed(777)
        self.assertEqual(consoleToCsv.getRandomNumber(1, 10), 4)

    def test_getRandomString(self):
        self.assertEqual(consoleToCsv.getRandomString(), "olsikryb")

    def test_generateName(self):
        self.assertTrue(len(consoleToCsv.generateName())>=3)

    def test_getGender(self):
        self.assertTrue(consoleToCsv.getGender() in consoleToCsv.genderList)

    def test_getSalution(self):
        self.assertTrue(consoleToCsv.getSalution(
            "M") in consoleToCsv.genderList["M"])
        self.assertTrue(consoleToCsv.getSalution(
            "F") in consoleToCsv.genderList["F"])

    def test_getCountry(self):
        self.assertTrue(consoleToCsv.getCountry() in consoleToCsv.countryList)

    def test_getCountryCode(self):
        self.assertTrue(consoleToCsv.getCountryCode("India")
                        in consoleToCsv.countryList["India"]["countryCode"])
        self.assertTrue(consoleToCsv.getCountryCode("China")
                        in consoleToCsv.countryList["China"]["countryCode"])
        self.assertTrue(consoleToCsv.getCountryCode("Malaysia")
                        in consoleToCsv.countryList["Malaysia"]["countryCode"])
        self.assertTrue(consoleToCsv.getCountryCode("Singapore")
                        in consoleToCsv.countryList["Singapore"]["countryCode"])

    def test_getMotherTongue(self):
        self.assertTrue(consoleToCsv.getMotherTongue("India")
                        in consoleToCsv.countryList["India"]["motherTongue"])
        self.assertTrue(consoleToCsv.getMotherTongue("China")
                        in consoleToCsv.countryList["China"]["motherTongue"])
        self.assertTrue(consoleToCsv.getMotherTongue("Malaysia")
                        in consoleToCsv.countryList["Malaysia"]["motherTongue"])
        self.assertTrue(consoleToCsv.getMotherTongue("Singapore")
                        in consoleToCsv.countryList["Singapore"]["motherTongue"])


if __name__ == '__main__':
    unittest.main()
