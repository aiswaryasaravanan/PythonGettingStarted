# read "input.txt" file and generate suggested email address and write to "output.txt" file

import csv


def getName(fname: str, lname: str):
    return fname + ' ' + lname


def getEmail(fname, lname, companyWebsite):
    return (fname + lname).casefold() + '@' + companyWebsite


def process(row: list):
    list1 = []
    list1.append(getName(row[0], row[1]))
    list1.append(getEmail(row[0], row[1], row[2]))
    return list1


with open("input.csv") as rCSV, open("output.csv", "w") as wCSV:
    try:
        readObj = csv.reader(rCSV)
        writeObj = csv.writer(wCSV)

        headerList = ["Name", "Suggested email"]
        writeObj.writerow(headerList)

        isFirst = True
        for line in readObj:
            if (isFirst):
                isFirst = False
                continue
            dataList = process(line)
            writeObj.writerow(dataList)

    except Exception:
        print("Error :(")
