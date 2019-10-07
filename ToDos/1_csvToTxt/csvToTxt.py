# read "input.txt" file and generate suggested email address and write to "output.txt" file

import csv
import unittest

def process(row,count):
    list1=[]
    if count==0:
        list1=["name","email"]
    else:
        list1.append(f'{" ".join([row[0],row[1]])}')
        list1.append(row[2])
    return list1

with open("input.csv") as rCSV, open("output.csv", "w") as wCSV:
    try:
        readObj = csv.reader(rCSV)
        writeObj=csv.writer(wCSV)
        count=0
        for row in readObj:
            list1=process(row,count)
            writeObj.writerow(list1)
            count=count+1
    except Exception:
        print("Error :(")



class tesingClass(unittest.TestCase):

    def test(self):
        self.assertEqual(process(["Andro","Babu","dbs.com"],1), ["Andro Babu","dbs.com"])
        self.assertEqual(process(["fname","lname","company website"],0), ["name","email"])


if __name__ == '__main__':
    unittest.main()