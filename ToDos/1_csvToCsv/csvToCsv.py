# read "input.txt" file and generate suggested email address and write to "output.txt" file

import csv


def getName(fname, lname):
    return f'{" ".join([row[0],row[1]])}'


def suggestEmail(fname, lname, companyWebsite):
    return f'{"@".join([(row[0]+row[1]).casefold(),row[2]])}'


def process(row):
    list1 = []
    list1.append(getName(row[0], row[1]))
    list1.append(suggestEmail(row[0], row[1], row[2]))
    return list1


with open("input.csv") as rCSV, open("output.csv", "w") as wCSV:
    try:
        readObj = csv.reader(rCSV)
        writeObj = csv.writer(wCSV)
        count = 0
        for row in readObj:
            if count == 0:
                list1 = ["Name", "Suggested email"]
            else:
                list1 = process(row)
            writeObj.writerow(list1)
            count = count+1
    except Exception:
        print("Error :(")
